import re
import subprocess

# Read data.ts to count equipment
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Count actual equipment entries
actual_count = len(re.findall(r"  id: '", content))

print(f"✅ عدد المعدات في التطبيق: {actual_count}")

# Extract all unique tag numbers from the application
app_tags = set()
for match in re.finditer(r"tagNo: '([^']+)'", content):
    tag = match.group(1)
    # Extract base tag (remove suffixes like A, B, -MOTOR, etc)
    base_tag = re.match(r'(\d{3}-[A-Z]+-\d+)', tag)
    if base_tag:
        app_tags.add(base_tag.group(1))

print(f"✅ عدد Tags الفريدة في التطبيق: {len(app_tags)}")

# Use PowerShell to extract tags from PDF
try:
    result = subprocess.run(
        ['powershell', '-Command', 
         "Select-String '\\d{3}[-/]\\w+-\\d+' 'pdf_content.txt' -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $_.Value }"],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    
    pdf_tags_raw = result.stdout.strip().split('\n')
    
    # Clean and normalize tags
    pdf_tags = set()
    for tag in pdf_tags_raw:
        tag = tag.strip().replace('/', '-')
        if re.match(r'\d{3}-\w+-\d+', tag):
            pdf_tags.add(tag)
    
    print(f"✅ عدد Tags في PDF: {len(pdf_tags)}")
    
    # Find truly missing tags (not in app even with A/B variants)
    truly_missing = []
    for pdf_tag in sorted(pdf_tags):
        # Check if base tag exists in any form
        has_variant = any(app_tag.startswith(pdf_tag) for app_tag in app_tags)
        if not has_variant and pdf_tag not in app_tags:
            truly_missing.append(pdf_tag)
    
    print(f"\n{'='*50}")
    if truly_missing:
        print(f"⚠️  Tags ناقصة فعلياً: {len(truly_missing)}")
        print("\n📋 القائمة:")
        for tag in truly_missing:
            print(f"   • {tag}")
    else:
        print("✅ جميع Tags من PDF موجودة في التطبيق!")
        print("   (بعضها مع suffixes مثل A/B)")
    
except Exception as e:
    print(f"❌ خطأ: {e}")
