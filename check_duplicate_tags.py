import re
import subprocess
from collections import defaultdict

# Extract all equipment entries from PDF with their parts
print("🔍 جاري استخراج جميع المعدات من PDF...\n")

with open('pdf_content.txt', 'r', encoding='utf-8', errors='ignore') as f:
    pdf_lines = f.readlines()

# Find all equipment entries with tag numbers and parts
equipment_entries = []
i = 0
while i < len(pdf_lines):
    line = pdf_lines[i].strip()
    # Look for tag number pattern
    if re.match(r'^\d{3}-[A-Z]+-\d+', line):
        tag = line.split()[0]
        # Get description and part from next lines
        desc = pdf_lines[i+1].strip() if i+1 < len(pdf_lines) else ""
        part = pdf_lines[i+2].strip() if i+2 < len(pdf_lines) else ""
        
        if desc and part:
            equipment_entries.append({
                'tag': tag,
                'description': desc,
                'part': part,
                'line': i+1
            })
    i += 1

print(f"✅ تم العثور على {len(equipment_entries)} معدة في PDF\n")

# Group by tag number
grouped = defaultdict(list)
for entry in equipment_entries:
    grouped[entry['tag']].append(entry)

# Read application data
with open('data.ts', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Find tags that appear multiple times in PDF
print("📋 Tag Numbers المتكررة في PDF:\n")
print("="*70)

missing_parts = []
for tag in sorted(grouped.keys()):
    entries = grouped[tag]
    if len(entries) > 1:
        print(f"\n🔧 {tag} - ({len(entries)} أجزاء)")
        for entry in entries:
            part_desc = entry['part']
            # Check if this part exists in app
            tag_pattern = f"tagNo: '{tag}'"
            part_pattern = f"part: '{part_desc}'" if part_desc else ""
            
            if tag_pattern in app_content:
                if part_pattern and part_pattern in app_content:
                    print(f"   ✓ {part_desc}")
                elif part_desc:
                    # Check for partial match
                    if any(p in app_content for p in part_desc.split()):
                        print(f"   ⚠️  {part_desc} (موجود بصيغة مختلفة)")
                    else:
                        print(f"   ✗ {part_desc} (ناقص)")
                        missing_parts.append({
                            'tag': tag,
                            'part': part_desc,
                            'description': entry['description']
                        })
            else:
                print(f"   ✗ {part_desc} (Tag ناقص)")
                missing_parts.append({
                    'tag': tag,
                    'part': part_desc,
                    'description': entry['description']
                })

print(f"\n{'='*70}")
print(f"\n📊 الإحصائيات:")
print(f"   • Tags متكررة في PDF: {sum(1 for k in grouped if len(grouped[k]) > 1)}")
print(f"   • إجمالي الأجزاء المتكررة: {sum(len(v) for k, v in grouped.items() if len(v) > 1)}")
print(f"   • الأجزاء الناقصة: {len(missing_parts)}")

if missing_parts:
    print(f"\n⚠️  الأجزاء الناقصة التي يجب إضافتها:")
    print("="*70)
    for item in missing_parts:
        print(f"\n   Tag: {item['tag']}")
        print(f"   Description: {item['description']}")
        print(f"   Part: {item['part']}")
