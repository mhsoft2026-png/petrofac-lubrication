import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment data for Winch and Crane components
new_equipment = """  },
  {
    id: '411-EAM-501-GEAR',
    tagNo: '411-EAM-501',
    description: 'Winch',
    part: 'Gear reducer',
    package: 'PFA411',
    type: LubricantType.OIL,
    grade: 'ISO VG 680',
    initialFill: '4.25 L',
    topUpQty: '4.25 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '25920 hrs',
    brands: { shell: "Omala S4 WE 680", mobil: "Mobil Glygoyle 68", other: "Klübersynth GH 6-680" },
    remarks: '1st fill shall be supplied along with equipment. It is compatible with suggested product. However, as standard practice it is advisable to flush existing fluid before filling new one'
  },
  {
    id: '300-Z-01-CROSS',
    tagNo: '300-Z-01',
    description: 'EOT Crane for Feed Gas Compressor Shelter',
    part: 'Cross Travel gearbox',
    package: 'PFM300',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '200 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '300-Z-01-LONG',
    tagNo: '300-Z-01',
    description: 'EOT Crane for Feed Gas Compressor Shelter',
    part: 'Long Travel gearbox',
    package: 'PFM300',
    type: LubricantType.OIL,
    grade: 'ISO VG 460',
    initialFill: '1 L',
    topUpQty: '0.25 L',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  }
];
"""

# Replace the closing bracket with new equipment
content = content.replace('  }\n];', new_equipment)

# Write updated content
with open('data.ts', 'w', encoding='utf-8') as f:
    f.write(content)

# Count equipment
equipment_count = len(re.findall(r"  id: '", content))
print(f"✅ تم إضافة 3 معدات جديدة (Winch & Crane Components)")
print(f"✅ إجمالي المعدات الآن: {equipment_count}")
