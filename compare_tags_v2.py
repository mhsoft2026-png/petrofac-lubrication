import re

# Read PDF content
try:
    with open('pdf_content.txt', 'r', encoding='utf-8') as f:
        pdf_lines = f.readlines()
except UnicodeDecodeError:
    with open('pdf_content.txt', 'r', encoding='latin-1') as f:
        pdf_lines = f.readlines()

# Extract all equipment tag numbers from PDF
# Patterns: 301-C-01, 301/302/303-C-01, 811-GT-01, etc.
pdf_tags_raw = set()
for line in pdf_lines:
    line = line.strip()
    # Pattern 1: XXX/XXX/XXX-XX-XX
    matches = re.findall(r'(\d{3}(?:/\d{3})*-[A-Z]+-\d{1,3}[A-Z]*)', line)
    pdf_tags_raw.update(matches)
    
    # Pattern 2: Simple XXX-XX-XX
    matches = re.findall(r'^(\d{3}-[A-Z]+-\d{1,3}[A-Z]*)$', line)
    pdf_tags_raw.update(matches)

# Expand multi-unit tags (301/302/303-C-01 -> 301-C-01, 302-C-01, 303-C-01)
pdf_tags_expanded = set()
for tag in pdf_tags_raw:
    if '/' in tag:
        # Split the prefix numbers
        parts = tag.split('-', 1)
        if len(parts) == 2:
            prefix_nums = parts[0].split('/')
            suffix = parts[1]
            for num in prefix_nums:
                pdf_tags_expanded.add(f"{num}-{suffix}")
    else:
        pdf_tags_expanded.add(tag)

# Read data.ts and extract tag numbers
with open('data.ts', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Extract unique tagNo values from data.ts
app_tags = set(re.findall(r"tagNo: '([^']+)'", data_content))

# Create base tags (without A/B/C suffixes) for comparison
pdf_base_tags = set()
for tag in pdf_tags_expanded:
    # Remove A, B, C, A/B, A/B/C suffixes
    base = re.sub(r'[A-C]$', '', tag)
    base = re.sub(r'A/B(?:/C)?$', '', base)
    pdf_base_tags.add(base)
    pdf_base_tags.add(tag)  # Keep original too

app_base_tags = set()
for tag in app_tags:
    # Remove -XXX suffixes used for parts (like -MOTOR, -BEARING, etc.)
    base = tag.split('-')[0:3]
    if len(base) >= 3:
        base_tag = '-'.join(base)
        app_base_tags.add(base_tag)
    app_base_tags.add(tag)

print(f"📊 تحليل Equipment Tag Numbers:")
print(f"═══════════════════════════════════")
print(f"✓ عدد Tags الأولية في PDF: {len(pdf_tags_raw)}")
print(f"✓ عدد Tags المتوسعة في PDF: {len(pdf_tags_expanded)}")
print(f"✓ عدد Tags الأساسية في PDF: {len(pdf_base_tags)}")
print(f"✓ عدد Tags في التطبيق: {len(app_tags)}")
print(f"✓ عدد Tags الأساسية في التطبيق: {len(app_base_tags)}")

# Find missing tags
missing_tags = pdf_base_tags - app_base_tags

print(f"\n⚠️  عدد Tags الناقصة: {len(missing_tags)}")

if missing_tags:
    print(f"\n📋 قائمة Tags الناقصة (أول 100):")
    print("═══════════════════════════════════")
    sorted_missing = sorted(list(missing_tags))[:100]
    for i, tag in enumerate(sorted_missing, 1):
        print(f"  {i:3d}. {tag}")
    
    if len(missing_tags) > 100:
        print(f"\n  ... و {len(missing_tags) - 100} معدات أخرى")

# Save all details
with open('missing_tags.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(missing_tags)))

with open('pdf_tags_all.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(pdf_tags_expanded)))

print(f"\n💾 تم حفظ البيانات:")
print(f"   - missing_tags.txt: القائمة الناقصة")
print(f"   - pdf_tags_all.txt: جميع tags من PDF")
