import re
import subprocess
from collections import defaultdict

print("="*70)
print("🔍 فحص شامل لجميع الصفحات من 1-12")
print("="*70)

# Read PDF content
with open('pdf_content.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    lines = content.split('\n')

# Find page markers
pages = []
for i, line in enumerate(lines):
    if ' of 12' in line:
        pages.append(i)

print(f"\n✅ تم العثور على {len(pages)} صفحة في PDF\n")

# Extract all tags using PowerShell
result = subprocess.run(
    ['powershell', '-Command',
     "Select-String '\\d{3}-[A-Z]+-\\d+' pdf_content.txt -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $_.Value }"],
    capture_output=True,
    text=True,
    encoding='utf-8'
)

pdf_tags_raw = [tag.strip() for tag in result.stdout.strip().split('\n') if tag.strip()]
pdf_tags = list(set([tag.replace('/', '-') for tag in pdf_tags_raw]))

print(f"📋 Tags في PDF:")
print(f"   • إجمالي ظهور Tags: {len(pdf_tags_raw)}")
print(f"   • Tags فريدة: {len(pdf_tags)}")

# Read application data
with open('data.ts', 'r', encoding='utf-8') as f:
    app_content = f.read()

app_tags = re.findall(r"tagNo: '([^']+)'", app_content)
unique_app_tags = set(app_tags)

print(f"\n📊 Tags في التطبيق:")
print(f"   • إجمالي المعدات: {len(app_tags)}")
print(f"   • Tags فريدة: {len(unique_app_tags)}")

# Find tags in PDF but not in app
missing = []
for pdf_tag in sorted(pdf_tags):
    # Check exact match
    if pdf_tag not in unique_app_tags:
        # Check if variants exist (A/B)
        has_variant = any(app_tag.startswith(pdf_tag) for app_tag in unique_app_tags)
        if not has_variant:
            missing.append(pdf_tag)

print(f"\n{'='*70}")
if missing:
    print(f"⚠️  Tags ناقصة: {len(missing)}")
    for tag in missing:
        print(f"   • {tag}")
else:
    print("✅ جميع Tags من PDF موجودة في التطبيق!")

# Analyze by package
print(f"\n{'='*70}")
print("📦 توزيع المعدات حسب Package:")
print("="*70)

package_count = defaultdict(int)
for match in re.finditer(r"package: '([^']+)'", app_content):
    package_count[match.group(1)] += 1

for package in sorted(package_count.keys()):
    count = package_count[package]
    print(f"   {package}: {count} معدة")

print(f"\n{'='*70}")
print("✅ الفحص مكتمل!")
print(f"📈 إحصائيات نهائية:")
print(f"   • Tags في PDF: {len(pdf_tags)}")
print(f"   • معدات في التطبيق: {len(app_tags)}")
print(f"   • Packages: {len(package_count)}")
print(f"   • Tags ناقصة: {len(missing)}")
print("="*70)
