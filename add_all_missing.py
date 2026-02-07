import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment data for missing items
new_equipment = """  },
  {
    id: '007-HAU-01A',
    tagNo: '007-HAU-01A',
    description: 'Air Handling Unit',
    part: 'Fan Shaft Bearing',
    package: 'PFA007',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '280 g',
    topUpQty: '50 g',
    topUpInterval: '10000 hrs',
    replacementInterval: '-',
    brands: { other: "SKF - LGMT 2 / SKF - LGMT 3 / SKF - LGWA 2" },
    remarks: '1. Grease shall be Base oil- Mineral Oil, Thickener- Lithium-calcium soap. 2. Based on grease condition interval to be decided'
  },
  {
    id: '008-HFU-01',
    tagNo: '008-HFU-01',
    description: 'Fresh Air Handling Unit',
    part: 'Fan Shaft Bearing',
    package: 'PFA008',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '60 g',
    topUpQty: '20 g',
    topUpInterval: '10000 hrs',
    replacementInterval: '-',
    brands: { other: "SKF - LGMT 2 / SKF - LGMT 3 / SKF - LGWA 2" },
    remarks: '1. Grease shall be Base oil- Mineral Oil, Thickener- Lithium-calcium soap. 2. Based on grease condition interval to be decided'
  },
  {
    id: '009-HFU-01',
    tagNo: '009-HFU-01',
    description: 'Fresh Air Handling Unit',
    part: 'Fan Shaft Bearing',
    package: 'PFA009',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '60 g',
    topUpQty: '20 g',
    topUpInterval: '10000 hrs',
    replacementInterval: '-',
    brands: { other: "SKF - LGMT 2 / SKF - LGMT 3 / SKF - LGWA 2" },
    remarks: '1. Grease shall be Base oil- Mineral Oil, Thickener- Lithium-calcium soap. 2. Based on grease condition interval to be decided'
  },
  {
    id: '010-HFU-01',
    tagNo: '010-HFU-01',
    description: 'Fresh Air Handling Unit',
    part: 'Fan Shaft Bearing',
    package: 'PFA010',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '60 g',
    topUpQty: '20 g',
    topUpInterval: '10000 hrs',
    replacementInterval: '-',
    brands: { other: "SKF - LGMT 2 / SKF - LGMT 3 / SKF - LGWA 2" },
    remarks: '1. Grease shall be Base oil- Mineral Oil, Thickener- Lithium-calcium soap. 2. Based on grease condition interval to be decided'
  },
  {
    id: '018-HFU-01',
    tagNo: '018-HFU-01',
    description: 'Fresh Air Handling Unit',
    part: 'Fan Shaft Bearing',
    package: 'PFA018',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '60 g',
    topUpQty: '20 g',
    topUpInterval: '10000 hrs',
    replacementInterval: '-',
    brands: { other: "SKF - LGMT 2 / SKF - LGMT 3 / SKF - LGWA 2" },
    remarks: '1. Grease shall be Base oil- Mineral Oil, Thickener- Lithium-calcium soap. 2. Based on grease condition interval to be decided'
  },
  {
    id: '019-HFU-01A',
    tagNo: '019-HFU-01A',
    description: 'Fresh Air Handling Unit',
    part: 'Fan Shaft Bearing',
    package: 'PFA019',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '60 g',
    topUpQty: '20 g',
    topUpInterval: '10000 hrs',
    replacementInterval: '-',
    brands: { other: "SKF - LGMT 2 / SKF - LGMT 3 / SKF - LGWA 2" },
    remarks: '1. Grease shall be Base oil- Mineral Oil, Thickener- Lithium-calcium soap. 2. Based on grease condition interval to be decided'
  },
  {
    id: '441-P-53A',
    tagNo: '441-P-53A',
    description: 'Waste Oil Transfer Pump',
    part: 'Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '441-P-53B',
    tagNo: '441-P-53B',
    description: 'Waste Oil Transfer Pump',
    part: 'Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '470-P-01S',
    tagNo: '470-P-01S',
    description: 'Instrument Air Supply Pump',
    part: 'Bearing',
    package: 'PFA470',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '480-P-01A',
    tagNo: '480-P-01A',
    description: 'Methanol Injection Pump',
    part: 'Bearing',
    package: 'PFA480',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '480-PM-01A',
    tagNo: '480-PM-01A',
    description: 'Methanol Injection Pump Motor',
    part: 'Bearing',
    package: 'PFA480',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '990-U-05B',
    tagNo: '990-U-05B',
    description: 'Unit Heater',
    part: 'Fan Bearing',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '990-U-06B',
    tagNo: '990-U-06B',
    description: 'Unit Heater',
    part: 'Fan Bearing',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '990-U-08B',
    tagNo: '990-U-08B',
    description: 'Unit Heater',
    part: 'Fan Bearing',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '990-U-11B',
    tagNo: '990-U-11B',
    description: 'Unit Heater',
    part: 'Fan Bearing',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '990-U-12B',
    tagNo: '990-U-12B',
    description: 'Unit Heater',
    part: 'Fan Bearing',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
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
print(f"✅ تم إضافة 16 معدة ناقصة")
print(f"✅ إجمالي المعدات الآن: {equipment_count}")
