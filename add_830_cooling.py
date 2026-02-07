import re

with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing Cooling System for 830-GD-01
new_equipment = """  {
    id: '830-GD-01-COOLING',
    tagNo: '830-GD-01',
    description: 'Diesel Engine',
    part: 'Cooling System',
    package: 'JI2045-0-PFM104',
    type: LubricantType.COOLANT,
    grade: 'ASTM D3306 (50% Mono Ethylene Glycol + 50% Potable Water)',
    initialFill: '1200 L',
    topUpQty: 'Refer Remark-1',
    topUpInterval: 'Refer Remark-1',
    replacementInterval: 'No fixed interval',
    brands: { shell: 'ROTELLA', mobil: 'HEAVY DUTY', total: 'COOLELF' },
    remarks: '1. No fixed interval - change when after check it looks degraded. 2. This equipment is a standby equipment and top-up is required to compensate any leakage during maintenance only. 3. First Fill of Glycol supplied by EDG Vendor.'
  },"""

# Insert after 830-GD-01
pattern = r"(id: '830-GD-01',[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    content = content[:match.end()] + "\n" + new_equipment + content[match.end():]
    
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    
    count = len(re.findall(r"  id: '", content))
    print(f"✅ تم إضافة Cooling System لـ 830-GD-01")
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 830-GD-01")
