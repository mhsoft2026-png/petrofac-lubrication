import subprocess
import re
from collections import defaultdict

print("🔍 استخراج جميع Tag Numbers من PDF...\n")

# Use PowerShell to extract all tags
result = subprocess.run(
    ['powershell', '-Command',
     "Select-String '\\d{3}-[A-Z]+-\\d+' pdf_content.txt -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $_.Value }"],
    capture_output=True,
    text=True,
    encoding='utf-8'
)

pdf_tags = result.stdout.strip().split('\n')
pdf_tags = [tag.strip() for tag in pdf_tags if tag.strip()]

print(f"✅ تم العثور على {len(pdf_tags)} tag في PDF\n")

# Count occurrences
tag_counts = defaultdict(int)
for tag in pdf_tags:
    tag_counts[tag] += 1

# Read app data
with open('data.ts', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Extract app tags
app_tags = re.findall(r"tagNo: '([^']+)'", app_content)
app_tag_counts = defaultdict(int)
for tag in app_tags:
    app_tag_counts[tag] += 1

print("="*70)
print("📊 Tag Numbers المتكررة في PDF:\n")

# Find tags that appear more than once in PDF
duplicates = {k: v for k, v in sorted(tag_counts.items()) if v > 1}

print(f"✅ عدد Tags المتكررة في PDF: {len(duplicates)}\n")

if duplicates:
    print("📋 القائمة الكاملة:\n")
    
    for tag, pdf_count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
        # Count in app
        app_count = app_tag_counts.get(tag, 0)
        
        # Also check for variants (A/B)
        variant_count = sum(1 for t in app_tags if t.startswith(tag))
        
        if variant_count >= pdf_count:
            status = "✓"
        elif app_count > 0:
            status = "⚠️"
        else:
            status = "✗"
            
        print(f"{status} {tag}: PDF={pdf_count}, App={app_count} (variants={variant_count})")

print(f"\n{'='*70}")
print("\n📈 الإحصائيات النهائية:")
print(f"   • إجمالي Tags في PDF: {len(tag_counts)}")
print(f"   • Tags متكررة: {len(duplicates)}")
print(f"   • إجمالي المعدات في التطبيق: {len(app_tags)}")
print(f"   • Tags فريدة في التطبيق: {len(set(app_tags))}")
