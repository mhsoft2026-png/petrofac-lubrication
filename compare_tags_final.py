import re

# Read PDF content
try:
    with open('pdf_content.txt', 'r', encoding='utf-8') as f:
        pdf_content = f.read()
except UnicodeDecodeError:
    with open('pdf_content.txt', 'r', encoding='latin-1') as f:
        pdf_content = f.read()

# Extract all equipment tag numbers from PDF using regex
# Pattern: digits/digits-LETTERS-digits
pdf_tags_raw = set()

# Pattern 1: Multi-unit tags like 301/302/303-C-01
pattern1 = r'\b(\d{3}(?:/\d{3})+)-([A-Z]+)-(\d{1,3}[A-Z/]*)\b'
matches1 = re.findall(pattern1, pdf_content)
for match in matches1:
    tag = f"{match[0]}-{match[1]}-{match[2]}"
    pdf_tags_raw.add(tag)

# Pattern 2: Simple tags like 754-C-01, 810-P-07
pattern2 = r'\b(\d{3})-([A-Z]+)-(\d{1,3}[A-Z/]*)\b'
matches2 = re.findall(pattern2, pdf_content)
for match in matches2:
    tag = f"{match[0]}-{match[1]}-{match[2]}"
    pdf_tags_raw.add(tag)

print(f"🔍 تم العثور على {len(pdf_tags_raw)} tag أولي في PDF")

# Expand multi-unit tags and A/B/C suffixes
pdf_tags_expanded = set()
for tag in pdf_tags_raw:
    parts = tag.split('-')
    if len(parts) >= 3:
        prefix = parts[0]
        middle = parts[1]
        suffix = '-'.join(parts[2:])
        
        # Handle multi-unit prefix (301/302/303)
        if '/' in prefix:
            units = prefix.split('/')
            for unit in units:
                base_tag = f"{unit}-{middle}-{suffix}"
                # Handle A/B/C suffix
                if '/A/B/C' in base_tag:
                    base = base_tag.replace('/A/B/C', '')
                    pdf_tags_expanded.add(f"{base}A")
                    pdf_tags_expanded.add(f"{base}B")
                    pdf_tags_expanded.add(f"{base}C")
                elif '/A/B' in base_tag:
                    base = base_tag.replace('/A/B', '')
                    pdf_tags_expanded.add(f"{base}A")
                    pdf_tags_expanded.add(f"{base}B")
                elif '/S' in base_tag:
                    base = base_tag.replace('/S', '')
                    pdf_tags_expanded.add(base)
                else:
                    pdf_tags_expanded.add(base_tag)
        else:
            # Single unit, just handle A/B/C suffix
            if '/A/B/C' in tag:
                base = tag.replace('/A/B/C', '')
                pdf_tags_expanded.add(f"{base}A")
                pdf_tags_expanded.add(f"{base}B")
                pdf_tags_expanded.add(f"{base}C")
            elif '/A/B' in tag:
                base = tag.replace('/A/B', '')
                pdf_tags_expanded.add(f"{base}A")
                pdf_tags_expanded.add(f"{base}B")
            elif '/S' in tag:
                base = tag.replace('/S', '')
                pdf_tags_expanded.add(base)
            else:
                pdf_tags_expanded.add(tag)

# Read data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Extract unique tagNo values
app_tags = set(re.findall(r"tagNo: '([^']+)'", data_content))

print(f"📊 تحليل Equipment Tag Numbers:")
print(f"═══════════════════════════════════")
print(f"✓ عدد Tags الأولية في PDF: {len(pdf_tags_raw)}")
print(f"✓ عدد Tags المتوسعة في PDF: {len(pdf_tags_expanded)}")
print(f"✓ عدد Tags الفريدة في التطبيق: {len(app_tags)}")

# Find missing tags
missing_tags = pdf_tags_expanded - app_tags

print(f"\n⚠️  عدد Tags الناقصة: {len(missing_tags)}")

if missing_tags:
    print(f"\n📋 قائمة Equipment Tags الناقصة:")
    print("═══════════════════════════════════")
    
    # Group by package number
    packages = {}
    for tag in sorted(missing_tags):
        pkg = tag.split('-')[0]
        if pkg not in packages:
            packages[pkg] = []
        packages[pkg].append(tag)
    
    for pkg in sorted(packages.keys()):
        tags_in_pkg = packages[pkg]
        print(f"\n  📦 Package {pkg}: ({len(tags_in_pkg)} معدات)")
        for tag in tags_in_pkg[:20]:  # Show first 20 per package
            print(f"     • {tag}")
        if len(tags_in_pkg) > 20:
            print(f"     ... + {len(tags_in_pkg) - 20} معدات أخرى")

# Save to files
with open('missing_tags.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(missing_tags)))

with open('pdf_tags_all.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(pdf_tags_expanded)))

print(f"\n💾 تم حفظ البيانات:")
print(f"   - missing_tags.txt: {len(missing_tags)} معدة ناقصة")
print(f"   - pdf_tags_all.txt: {len(pdf_tags_expanded)} معدة من PDF")
