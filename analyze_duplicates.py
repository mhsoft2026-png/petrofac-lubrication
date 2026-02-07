import re
from collections import defaultdict

print("🔍 جاري فحص جميع المعدات في PDF بدقة...\n")

with open('pdf_content.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find all tag numbers in the PDF
tag_pattern = r'(\d{3}[-/][A-Z]+[-/]\d+(?:[A-Z/]+)?)'
all_tags = re.findall(tag_pattern, content)

# Normalize tags (replace / with -)
normalized_tags = [tag.replace('/', '-') for tag in all_tags]

# Count occurrences
tag_count = defaultdict(int)
for tag in normalized_tags:
    # Extract base tag without A/B suffix
    base = re.match(r'(\d{3}-[A-Z]+-\d+)', tag)
    if base:
        tag_count[base.group(1)] += 1

print(f"✅ تم العثور على {len(all_tags)} ذكر لـ tag numbers في PDF")
print(f"✅ عدد Tags الفريدة: {len(tag_count)}\n")

# Read application data
with open('data.ts', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Extract all equipment from app
app_equipment = []
pattern = r"{\s*id: '([^']+)',\s*tagNo: '([^']+)',\s*description: '([^']+)',\s*part: '([^']+)'"
for match in re.finditer(pattern, app_content):
    app_equipment.append({
        'id': match.group(1),
        'tag': match.group(2),
        'description': match.group(3),
        'part': match.group(4)
    })

print(f"✅ عدد المعدات في التطبيق: {len(app_equipment)}\n")

# Group app equipment by tag
app_by_tag = defaultdict(list)
for eq in app_equipment:
    app_by_tag[eq['tag']].append(eq)

# Show tags that appear multiple times
print("="*70)
print("📋 Tag Numbers التي تظهر أكثر من مرة:\n")

duplicates_in_pdf = {k: v for k, v in tag_count.items() if v > 1}
duplicates_in_app = {k: v for k, v in app_by_tag.items() if len(v) > 1}

print(f"🔧 في PDF: {len(duplicates_in_pdf)} tag متكرر")
for tag in sorted(duplicates_in_pdf.keys())[:10]:  # Show first 10
    count = duplicates_in_pdf[tag]
    app_count = len(app_by_tag.get(tag, []))
    status = "✓" if app_count >= count else "⚠️"
    print(f"   {status} {tag}: {count} مرة في PDF, {app_count} في التطبيق")

print(f"\n🔧 في التطبيق: {len(duplicates_in_app)} tag متكرر")
for tag in sorted(duplicates_in_app.keys())[:10]:  # Show first 10
    parts = [eq['part'] for eq in app_by_tag[tag]]
    print(f"   • {tag}: {len(parts)} جزء - {', '.join(parts[:3])}{'...' if len(parts) > 3 else ''}")

# Check for missing duplicates
print(f"\n{'='*70}")
print("⚠️  Tags التي تحتاج فحص إضافي:\n")

needs_review = []
for tag, pdf_count in duplicates_in_pdf.items():
    app_count = len(app_by_tag.get(tag, []))
    if app_count < pdf_count:
        needs_review.append((tag, pdf_count, app_count))

if needs_review:
    for tag, pdf_count, app_count in sorted(needs_review)[:20]:
        print(f"   {tag}: PDF={pdf_count}, App={app_count} (نقص {pdf_count - app_count})")
else:
    print("   ✅ جميع Tags المتكررة موجودة بشكل كامل!")
