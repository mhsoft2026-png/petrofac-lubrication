import re

# Read data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment to add for 300-Z-01 Ex Control Panel
new_equipment = """  {
    id: '300-Z-01-EX-PANEL',
    tagNo: '300-Z-01',
    description: 'EOT Crane for Feed Gas Compressor Shelter',
    part: 'Ex control panel enclosure',
    package: 'PFM110',
    type: LubricantType.GREASE,
    grade: 'ISO 2137 (Copper Grease)',
    initialFill: '100 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '8640 hrs',
    brands: { other: '3 In One Anti-Seize Copper Grease / Fuchs-PBC/DGrease Anti-Seize' },
    remarks: '1. Inspect/check/ clean & relube Ex gap at 12 month. 2. Initial fill is by package vendor'
  },"""

# Find the position after 300-Z-01-SPRINGS
pattern = r"(id: '300-Z-01-SPRINGS'[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    # Insert new equipment after 300-Z-01-SPRINGS
    insert_pos = match.end()
    updated_content = content[:insert_pos] + "\n" + new_equipment + content[insert_pos:]
    
    # Write back
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ تم إضافة 300-Z-01-EX-PANEL")
    
    # Count total equipment
    count = len(re.findall(r"  id: '", updated_content))
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 300-Z-01-SPRINGS")
