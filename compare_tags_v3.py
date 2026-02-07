import re

# Read PDF content
try:
    with open('pdf_content.txt', 'r', encoding='utf-8') as f:
        pdf_lines = f.readlines()
except UnicodeDecodeError:
    with open('pdf_content.txt', 'r', encoding='latin-1') as f:
        pdf_lines = f.readlines()

# Extract all equipment tag numbers from PDF
# Looking for lines that start with a tag pattern
pdf_tags_raw = set()
for line in pdf_lines:
    line = line.strip()
    # Match lines starting with XXX-XX-XXX pattern
    match = re.match(r'^(\d{3}(?:/\d{3})*-[A-Z]+-\d{1,3}[A-Z/]*)', line)
    if match:
        pdf_tags_raw.add(match.group(1))

# Expand multi-unit tags (301/302/303-C-01 -> 301-C-01, 302-C-01, 303-C-01)
pdf_tags_expanded = set()
for tag in pdf_tags_raw:
    if '/' in tag and tag[0].isdigit():
        # Check if slash is in the prefix (unit numbers)
        parts = tag.split('-')
        if len(parts) >= 2 and '/' in parts[0]:
            # Multiple units
            unit_nums = parts[0].split('/')
            suffix = '-'.join(parts[1:])
            for num in unit_nums:
                expanded_tag = f"{num}-{suffix}"
                # Handle A/B/C suffixes
                if '/A/B/C' in expanded_tag:
                    base = expanded_tag.replace('/A/B/C', '')
                    pdf_tags_expanded.add(f"{base}A")
                    pdf_tags_expanded.add(f"{base}B")
                    pdf_tags_expanded.add(f"{base}C")
                elif '/A/B' in expanded_tag:
                    base = expanded_tag.replace('/A/B', '')
                    pdf_tags_expanded.add(f"{base}A")
                    pdf_tags_expanded.add(f"{base}B")
                else:
                    pdf_tags_expanded.add(expanded_tag)
        else:
            # Handle suffix A/B/C
            if '/A/B/C' in tag:
                base = tag.replace('/A/B/C', '')
                pdf_tags_expanded.add(f"{base}A")
                pdf_tags_expanded.add(f"{base}B")
                pdf_tags_expanded.add(f"{base}C")
            elif '/A/B' in tag:
                base = tag.replace('/A/B', '')
                pdf_tags_expanded.add(f"{base}A")
                pdf_tags_expanded.add(f"{base}B")
            else:
                pdf_tags_expanded.add(tag)
    else:
        pdf_tags_expanded.add(tag)

# Read data.ts and extract tag numbers
with open('data.ts', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Extract unique tagNo values from data.ts (base equipment tags only, not parts)
app_tags_all = re.findall(r"tagNo: '([^']+)'", data_content)
app_tags = set(app_tags_all)

# Extract just base equipment tags (first occurrence of each tagNo)
app_base_equipment = {}
for tag in app_tags_all:
    # Remove suffixes like -MOTOR, -BEARING, -SEAL, etc. to get base tag
    if tag not in app_base_equipment:
        app_base_equipment[tag] = True

print(f"📊 تحليل Equipment Tag Numbers:")
print(f"═══════════════════════════════════")
print(f"✓ عدد Tags الأولية في PDF: {len(pdf_tags_raw)}")
print(f"✓ عدد Tags المتوسعة في PDF: {len(pdf_tags_expanded)}")
print(f"✓ عدد Tags الفريدة في التطبيق: {len(app_tags)}")
print(f"✓ عدد معدات في التطبيق (إجمالي): {len(app_tags_all)}")

# Find missing tags - compare PDF tags with app base tags
missing_tags = pdf_tags_expanded - app_tags

print(f"\n⚠️  عدد Tags الناقصة: {len(missing_tags)}")

if missing_tags:
    print(f"\n📋 قائمة Equipment Tags الناقصة:")
    print("═══════════════════════════════════")
    sorted_missing = sorted(list(missing_tags))
    
    # Group by package
    packages = {}
    for tag in sorted_missing:
        pkg = tag.split('-')[0]
        if pkg not in packages:
            packages[pkg] = []
        packages[pkg].append(tag)
    
    total_shown = 0
    for pkg in sorted(packages.keys()):
        print(f"\n  📦 Package {pkg}:")
        for tag in sorted(packages[pkg]):
            if total_shown < 100:
                print(f"     • {tag}")
                total_shown += 1
    
    if len(missing_tags) > 100:
        print(f"\n  ... و {len(missing_tags) - 100} معدات أخرى")

# Save details
with open('missing_tags.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(missing_tags)))

with open('pdf_tags_all.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(pdf_tags_expanded)))

print(f"\n💾 تم حفظ البيانات:")
print(f"   - missing_tags.txt: {len(missing_tags)} معدة ناقصة")
print(f"   - pdf_tags_all.txt: {len(pdf_tags_expanded)} معدة من PDF")
