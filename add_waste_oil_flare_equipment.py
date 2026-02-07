import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment data for Waste Oil Package (441) and Flare Package (414)
new_equipment = """  },
  {
    id: '441-M-51',
    tagNo: '441-M-51',
    description: 'Recovered Oil Pit Mixer',
    part: 'Reducer',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 220',
    initialFill: '3.9 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '10000 hrs',
    brands: ['Castrol Alphasyn EP 220', 'ENI BLASIA 220'],
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-M-52',
    tagNo: '441-M-52',
    description: 'Inlet Mixing Chamber Mixer',
    part: 'Reducer',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 220',
    initialFill: '3.9 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '10000 hrs',
    brands: ['Castrol Alphasyn EP 220', 'ENI BLASIA 220'],
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-03A-PUMP',
    tagNo: '441-P-03A',
    description: 'Waste Oil Pump',
    part: 'Pump Bearings',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 3',
    initialFill: '70 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: ['Alvania Fett R3', 'Mobilux 3', 'Unirex N3', 'Esso Beacon 3'],
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-03A-MOTOR',
    tagNo: '441-P-03A',
    description: 'Waste Oil Pump',
    part: 'Motor Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['-'],
    remarks: 'Greased For Life'
  },
  {
    id: '441-P-03B-PUMP',
    tagNo: '441-P-03B',
    description: 'Waste Oil Pump',
    part: 'Pump Bearings',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 3',
    initialFill: '70 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: ['Alvania Fett R3', 'Mobilux 3', 'Unirex N3', 'Esso Beacon 3'],
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-03B-MOTOR',
    tagNo: '441-P-03B',
    description: 'Waste Oil Pump',
    part: 'Motor Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['-'],
    remarks: 'Greased For Life'
  },
  {
    id: '414-P-04A-DRIVE',
    tagNo: '414-P-04A',
    description: 'Disposal Flare Pump',
    part: 'Pump Drive End',
    package: 'PFA414',
    type: LubricantType.OIL,
    grade: 'ISO VG 220',
    initialFill: '0.95 L',
    topUpQty: '0.95 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '4320 hrs',
    brands: ['Alphasyn EP 220', 'Omala S4 GXV 220', 'Mobil SHC Gear 220', 'MAK-220'],
    remarks: '1st fill shall be supplied along with equipment. It is compatible with suggested product. However, as standard practice it is advisable to flush existing fluid before filling new one'
  },
  {
    id: '414-P-04A-DRDS',
    tagNo: '414-P-04A',
    description: 'Disposal Flare Pump',
    part: 'Pump DRDS Oil',
    package: 'PFA414',
    type: LubricantType.OIL,
    grade: 'ISO VG 220',
    initialFill: '0.05 L',
    topUpQty: '0.05 L',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['Alphasyn EP 220', 'Omala S4 GXV 220', 'Mobil SHC Gear 220', 'MAK-220'],
    remarks: '1st fill shall be supplied along with equipment. Oil replacement is required in the event of diaphragm rupture'
  },
  {
    id: '414-P-04A-MOTOR',
    tagNo: '414-P-04A',
    description: 'Disposal Flare Pump',
    part: 'Pump Motor-Bearing',
    package: 'PFA414',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['NLGI-2'],
    remarks: '1st fill shall be supplied along with equipment. Greased for Life.'
  },
  {
    id: '414-P-04B-DRIVE',
    tagNo: '414-P-04B',
    description: 'Disposal Flare Pump',
    part: 'Pump Drive End',
    package: 'PFA414',
    type: LubricantType.OIL,
    grade: 'ISO VG 220',
    initialFill: '0.95 L',
    topUpQty: '0.95 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '4320 hrs',
    brands: ['Alphasyn EP 220', 'Omala S4 GXV 220', 'Mobil SHC Gear 220', 'MAK-220'],
    remarks: '1st fill shall be supplied along with equipment. It is compatible with suggested product. However, as standard practice it is advisable to flush existing fluid before filling new one'
  },
  {
    id: '414-P-04B-DRDS',
    tagNo: '414-P-04B',
    description: 'Disposal Flare Pump',
    part: 'Pump DRDS Oil',
    package: 'PFA414',
    type: LubricantType.OIL,
    grade: 'ISO VG 220',
    initialFill: '0.05 L',
    topUpQty: '0.05 L',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['Alphasyn EP 220', 'Omala S4 GXV 220', 'Mobil SHC Gear 220', 'MAK-220'],
    remarks: '1st fill shall be supplied along with equipment. Oil replacement is required in the event of diaphragm rupture'
  },
  {
    id: '414-P-04B-MOTOR',
    tagNo: '414-P-04B',
    description: 'Disposal Flare Pump',
    part: 'Pump Motor-Bearing',
    package: 'PFA414',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['NLGI-2'],
    remarks: '1st fill shall be supplied along with equipment. Greased for Life.'
  },
  {
    id: '411-EAM-501',
    tagNo: '411-EAM-501',
    description: 'Winch',
    part: 'Winch motor',
    package: 'PFA411',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['NLGI-2'],
    remarks: 'Greased for Life'
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
print(f"✅ تم إضافة 13 معدة جديدة من Waste Oil Package (441) و Flare Package (414)")
print(f"✅ إجمالي المعدات الآن: {equipment_count}")
