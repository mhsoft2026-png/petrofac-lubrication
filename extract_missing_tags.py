import re
import subprocess

# Use PowerShell to extract tags (more reliable for this format)
ps_command = r"Get-Content pdf_content.txt | Select-String '\d{3}[-/]\w+-\d+[A-Z]*' -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $_.Value } | Sort-Object -Unique"

result = subprocess.run(['powershell', '-Command', ps_command], capture_output=True, text=True, encoding='utf-8')
pdf_tags_raw = set(result.stdout.strip().split('\n'))
pdf_tags_raw = {tag.strip() for tag in pdf_tags_raw if tag.strip()}

print(f"🔍 تم العثور على {len(pdf_tags_raw)} tag في PDF")

# Expand multi-unit and A/B/C patterns
pdf_tags_expanded = set()
for tag in pdf_tags_raw:
    if not tag or not re.match(r'\d', tag):
        continue
        
    # Handle multi-unit tags (301/302/303-XX-XX)
    if '/' in tag and tag[0].isdigit():
        parts = tag.split('-')
        if len(parts) >= 2 and '/' in parts[0]:
            units = parts[0].split('/')
            suffix = '-'.join(parts[1:])
            for unit in units:
                expanded = f"{unit}-{suffix}"
                pdf_tags_expanded.add(expanded)
        else:
            pdf_tags_expanded.add(tag)
    else:
        pdf_tags_expanded.add(tag)

# Read data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Extract tagNo values
app_tags = set(re.findall(r"tagNo: '([^']+)'", data_content))

print(f"\n📊 تحليل Equipment Tag Numbers:")
print(f"═══════════════════════════════════")
print(f"✓ Tags في PDF: {len(pdf_tags_raw)}")
print(f"✓ Tags متوسعة في PDF: {len(pdf_tags_expanded)}")
print(f"✓ Tags فريدة في التطبيق: {len(app_tags)}")
print(f"✓ إجمالي المعدات في التطبيق: 791")

# Find missing
missing = pdf_tags_expanded - app_tags

print(f"\n⚠️  عدد Tags الناقصة: {len(missing)}")

if missing:
    # Group by package
    packages = {}
    for tag in missing:
        pkg = tag.split('-')[0] if '-' in tag else 'other'
        if pkg not in packages:
            packages[pkg] = []
        packages[pkg].append(tag)
    
    print(f"\n📋 Equipment Tags الناقصة حسب Package:")
    print("═══════════════════════════════════")
    
    for pkg in sorted(packages.keys()):
        tags = sorted(packages[pkg])
        print(f"\n  📦 Package {pkg}: ({len(tags)} معدات)")
        for t in tags[:15]:
            print(f"     • {t}")
        if len(tags) > 15:
            print(f"     ... + {len(tags) - 15} معدات")

# Save
with open('missing_tags.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(missing)))

print(f"\n💾 تم حفظ {len(missing)} tag ناقص في missing_tags.txt")
