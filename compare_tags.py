import re

# Read PDF content
try:
    with open('pdf_content.txt', 'r', encoding='utf-8') as f:
        pdf_content = f.read()
except UnicodeDecodeError:
    with open('pdf_content.txt', 'r', encoding='latin-1') as f:
        pdf_content = f.read()

# Extract all equipment tag numbers from PDF (patterns like XXX-X-XX)
# Looking for patterns: digits-letters-digits or similar
tag_patterns = [
    r'\b(\d{3}-[A-Z]+-\d{2}[A-Z]?(?:/[A-Z])?)\b',  # 301-EA-01A/B
    r'\b(\d{3}-[A-Z]+-\d{2})\b',                     # 301-P-01
    r'\b(\d{3}-[A-Z]{1,3}-\d{1,3})\b',              # 421-C-01, 830-GD-01
]

pdf_tags = set()
for pattern in tag_patterns:
    matches = re.findall(pattern, pdf_content)
    pdf_tags.update(matches)

# Clean up tags - handle A/B, A/B/C notation
cleaned_pdf_tags = set()
for tag in pdf_tags:
    # Remove /S, /A/B, /A/B/C suffixes for comparison
    base_tag = re.sub(r'/[A-Z/]+$', '', tag)
    cleaned_pdf_tags.add(base_tag)
    
    # If tag has /A/B pattern, add individual tags
    if '/A/B/C' in tag:
        base = tag.replace('/A/B/C', '')
        cleaned_pdf_tags.add(f"{base}A")
        cleaned_pdf_tags.add(f"{base}B")
        cleaned_pdf_tags.add(f"{base}C")
    elif '/A/B' in tag:
        base = tag.replace('/A/B', '')
        cleaned_pdf_tags.add(f"{base}A")
        cleaned_pdf_tags.add(f"{base}B")

# Read data.ts and extract tag numbers
with open('data.ts', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Extract tagNo values from data.ts
app_tags = set(re.findall(r"tagNo: '([^']+)'", data_content))

# Also extract base tags without suffixes for comparison
app_base_tags = set()
for tag in app_tags:
    base_tag = re.sub(r'[A-Z]$', '', tag)  # Remove single letter suffix
    app_base_tags.add(base_tag)
    app_base_tags.add(tag)

print(f"📊 تحليل Equipment Tag Numbers:")
print(f"═══════════════════════════════════")
print(f"✓ عدد Tags في ملف PDF: {len(cleaned_pdf_tags)}")
print(f"✓ عدد Tags في التطبيق: {len(app_tags)}")
print(f"✓ عدد Tags الأساسية في التطبيق: {len(app_base_tags)}")

# Find missing tags
missing_tags = cleaned_pdf_tags - app_base_tags

print(f"\n⚠️  عدد Tags الناقصة: {len(missing_tags)}")

if missing_tags:
    print(f"\n📋 قائمة Tags الناقصة (أول 50):")
    print("═══════════════════════════════════")
    sorted_missing = sorted(list(missing_tags))[:50]
    for i, tag in enumerate(sorted_missing, 1):
        print(f"  {i:2d}. {tag}")
    
    if len(missing_tags) > 50:
        print(f"  ... و {len(missing_tags) - 50} معدات أخرى")

# Save missing tags to file for further processing
with open('missing_tags.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(missing_tags)))

print(f"\n💾 تم حفظ قائمة Tags الناقصة في: missing_tags.txt")
