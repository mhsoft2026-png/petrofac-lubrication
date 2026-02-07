#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add ALL missing equipment to the database
This adds: Motor pumps, Seal cooler motors, Additional crane equipment, and more
"""

def read_current_data():
    """Read current data.ts and extract existing IDs"""
    try:
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract all existing IDs
            import re
            ids = re.findall(r"id: '([^']+)'", content)
            return set(ids), content
    except:
        return set(), ""

def generate_additional_equipment():
    """Generate all missing equipment entries"""
    
    existing_ids, current_content = read_current_data()
    
    new_entries = []
    
    print("="*80)
    print("إضافة المعدات المفقودة")
    print("="*80)
    
    # ========================================
    # PUMP MOTORS (Missing from PFM106)
    # ========================================
    print("\n[1] إضافة محركات المضخات...")
    
    pump_motors = [
        # Hot Oil System
        ('401-PM-01A', '401-P-01A', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-01B', '401-P-01B', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-01C', '401-P-01C', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-01D', '401-P-01D', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-02', '401-P-02', 'Hot Oil Drain Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-03', '401-P-03', 'Hot Oil Storage Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        # Flare Systems
        ('411-PM-01A', '411-P-01A', 'High Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('411-PM-01B', '411-P-01B', 'High Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('412-PM-02A', '412-P-02A', 'Cold Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('412-PM-02B', '412-P-02B', 'Cold Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('413-PM-03A', '413-P-03A', 'Low Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('413-PM-03B', '413-P-03B', 'Low Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('442-PM-01', '442-P-01', 'Closed Drain Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '5000 hrs (DE) / 5000 hrs (NDE)'),
        # Deethanizer System
        ('520-PM-02A', '520-P-02A', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('520-PM-02B', '520-P-02B', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('620-PM-02A', '620-P-02A', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('620-PM-02B', '620-P-02B', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        # LPG System
        ('530-PM-03A', '530-P-03A', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('530-PM-03B', '530-P-03B', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('630-PM-03A', '630-P-03A', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('630-PM-03B', '630-P-03B', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-04A', '730-P-04A', 'LPG Booster/Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-04B', '730-P-04B', 'LPG Booster/Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-04C', '730-P-04C', 'LPG Booster/Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        # Wash Column
        ('520-PM-01A', '520-P-01A', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('520-PM-01B', '520-P-01B', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('620-PM-01A', '620-P-01A', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('620-PM-01B', '620-P-01B', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        # Condensate System
        ('710-PM-01A', '710-P-01A', 'Condensate Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-01B', '710-P-01B', 'Condensate Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-02A', '710-P-02A', 'Off-Spec Condensate Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-02B', '710-P-02B', 'Off-Spec Condensate Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-03A', '710-P-03A', 'Condensate Pipeline Booster Pump Motor', 'NLGI Grade 2', '34 g (DE) / 34 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('710-PM-03B', '710-P-03B', 'Condensate Pipeline Booster Pump Motor', 'NLGI Grade 2', '34 g (DE) / 34 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        # LPG Pipeline
        ('730-PM-05A', '730-P-05A', 'LPG Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-05B', '730-P-05B', 'LPG Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-05C', '730-P-05C', 'LPG Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-06', '730-P-06', 'LPG Spiking Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
    ]
    
    count = 0
    for motor_id, pump_tag, desc, grade, init_fill, repl_int in pump_motors:
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '{motor_id}',
    description: '{desc}',
    part: 'Bearings',
    package: 'JI2045-0-PFM106',
    type: LubricantType.GREASE,
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{repl_int}',
    brands: {{ shell: 'GADUS S5 V100 2', mobil: 'MOBILITH SHC 100', total: 'MULTIPLEX S 2 A', other: 'KLUBERPLEX BEM 41-132' }},
    remarks: ''
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} محرك مضخة")
    
    # ========================================
    # SEAL COOLER MOTORS
    # ========================================
    print("[2] إضافة محركات مبردات الختم...")
    
    seal_cooler_motors = [
        ('401-P-01A-SEAL-MOTOR', '401-P-01A', 'Hot Oil Circulation Pump Seal Cooler Motor'),
        ('401-P-01B-SEAL-MOTOR', '401-P-01B', 'Hot Oil Circulation Pump Seal Cooler Motor'),
        ('401-P-01C-SEAL-MOTOR', '401-P-01C', 'Hot Oil Circulation Pump Seal Cooler Motor'),
        ('401-P-01D-SEAL-MOTOR', '401-P-01D', 'Hot Oil Circulation Pump Seal Cooler Motor'),
        ('401-P-02-SEAL-MOTOR', '401-P-02', 'Hot Oil Drain Pump Seal Cooler Motor'),
        ('401-P-03-SEAL-MOTOR', '401-P-03', 'Hot Oil Storage Pump Seal Cooler Motor'),
        ('730-P-04A-SEAL-MOTOR', '730-P-04A', 'LPG Booster/Return Pump Seal Cooler Motor'),
        ('730-P-04B-SEAL-MOTOR', '730-P-04B', 'LPG Booster/Return Pump Seal Cooler Motor'),
        ('730-P-04C-SEAL-MOTOR', '730-P-04C', 'LPG Booster/Return Pump Seal Cooler Motor'),
        ('710-P-01A-SEAL-MOTOR', '710-P-01A', 'Condensate Pipeline Pump Seal Cooler Motor'),
        ('710-P-01B-SEAL-MOTOR', '710-P-01B', 'Condensate Pipeline Pump Seal Cooler Motor'),
        ('730-P-06-SEAL-MOTOR1', '730-P-06', 'LPG Spiking Pump Seal Cooler Motor'),
        ('730-P-06-SEAL-MOTOR2', '730-P-06', 'LPG Spiking Pump Seal Cooler Motor'),
        ('730-P-05A-SEAL-MOTOR1', '730-P-05A', 'LPG Pipeline Pump Seal Cooler Motor'),
        ('730-P-05A-SEAL-MOTOR2', '730-P-05A', 'LPG Pipeline Pump Seal Cooler Motor'),
        ('730-P-05B-SEAL-MOTOR1', '730-P-05B', 'LPG Pipeline Pump Seal Cooler Motor'),
        ('730-P-05B-SEAL-MOTOR2', '730-P-05B', 'LPG Pipeline Pump Seal Cooler Motor'),
        ('730-P-05C-SEAL-MOTOR1', '730-P-05C', 'LPG Pipeline Pump Seal Cooler Motor'),
        ('730-P-05C-SEAL-MOTOR2', '730-P-05C', 'LPG Pipeline Pump Seal Cooler Motor'),
        ('710-P-02A-SEAL-MOTOR', '710-P-02A', 'Off-Spec Condensate Return Pump Seal Cooler Motor'),
        ('710-P-02B-SEAL-MOTOR', '710-P-02B', 'Off-Spec Condensate Return Pump Seal Cooler Motor'),
    ]
    
    count = 0
    for motor_id, pump_tag, desc in seal_cooler_motors:
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '{pump_tag}',
    description: '{desc}',
    part: 'Bearings',
    package: 'JI2045-0-PFM108',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} محرك مبرد ختم")
    
    # ========================================
    # ADDITIONAL SEAL ACCUMULATORS
    # ========================================
    print("[3] إضافة Seal Accumulators الإضافية...")
    
    seal_accumulators = [
        ('520-P-02A-SEAL-ACC', '520-P-02A', 'Deethanizer Reflux Pump', 'PROPYL ALCOHOL', '35.18 L', '27.70 L'),
        ('520-P-02B-SEAL-ACC', '520-P-02B', 'Deethanizer Reflux Pump', 'PROPYL ALCOHOL', '35.18 L', '27.70 L'),
        ('620-P-02A-SEAL-ACC', '620-P-02A', 'Deethanizer Reflux Pump', 'PROPYL ALCOHOL', '35.18 L', '27.70 L'),
        ('620-P-02B-SEAL-ACC', '620-P-02B', 'Deethanizer Reflux Pump', 'PROPYL ALCOHOL', '35.18 L', '27.70 L'),
        ('530-P-03A-SEAL-ACC', '530-P-03A', 'LPG Product/Reflux Pump', 'PROPYL ALCOHOL', '34.7 L', '27.20 L'),
        ('530-P-03B-SEAL-ACC', '530-P-03B', 'LPG Product/Reflux Pump', 'PROPYL ALCOHOL', '34.7 L', '27.20 L'),
        ('630-P-03A-SEAL-ACC', '630-P-03A', 'LPG Product/Reflux Pump', 'PROPYL ALCOHOL', '34.7 L', '27.20 L'),
        ('630-P-03B-SEAL-ACC', '630-P-03B', 'LPG Product/Reflux Pump', 'PROPYL ALCOHOL', '34.7 L', '27.20 L'),
        ('730-P-04A-SEAL-ACC', '730-P-04A', 'LPG Booster/Return Pump', 'PROPYL ALCOHOL', '41.4 L', '27.20 L'),
        ('730-P-04B-SEAL-ACC', '730-P-04B', 'LPG Booster/Return Pump', 'PROPYL ALCOHOL', '41.4 L', '27.20 L'),
        ('730-P-04C-SEAL-ACC', '730-P-04C', 'LPG Booster/Return Pump', 'PROPYL ALCOHOL', '41.4 L', '27.20 L'),
        ('520-P-01A-SEAL-ACC', '520-P-01A', 'Wash Column Pump', 'PROPYL ALCOHOL', '33.3 L', '25.80 L'),
        ('520-P-01B-SEAL-ACC', '520-P-01B', 'Wash Column Pump', 'PROPYL ALCOHOL', '33.3 L', '25.80 L'),
        ('620-P-01A-SEAL-ACC', '620-P-01A', 'Wash Column Pump', 'PROPYL ALCOHOL', '33.3 L', '25.80 L'),
        ('620-P-01B-SEAL-ACC', '620-P-01B', 'Wash Column Pump', 'PROPYL ALCOHOL', '33.3 L', '25.80 L'),
        ('710-P-01A-SEAL-ACC', '710-P-01A', 'Condensate Pipeline Pump', 'ISO VG 10', '56.28 L', '27.30 L'),
        ('710-P-01B-SEAL-ACC', '710-P-01B', 'Condensate Pipeline Pump', 'ISO VG 10', '56.28 L', '27.30 L'),
        ('730-P-06-SEAL-ACC', '730-P-06', 'LPG Spiking Pump', 'PROPYL ALCOHOL', '103.08 L', '68.72 L'),
        ('730-P-05A-SEAL-ACC', '730-P-05A', 'LPG Pipeline Pump', 'PROPYL ALCOHOL', '126.4 L', '88.86 L'),
        ('730-P-05B-SEAL-ACC', '730-P-05B', 'LPG Pipeline Pump', 'PROPYL ALCOHOL', '126.4 L', '88.86 L'),
        ('730-P-05C-SEAL-ACC', '730-P-05C', 'LPG Pipeline Pump', 'PROPYL ALCOHOL', '126.4 L', '88.86 L'),
        ('710-P-02A-SEAL-ACC', '710-P-02A', 'Off-Spec Condensate Return Pump', 'ISO VG 10', '48.8 L', '30.03 L'),
        ('710-P-02B-SEAL-ACC', '710-P-02B', 'Off-Spec Condensate Return Pump', 'ISO VG 10', '48.8 L', '30.03 L'),
        ('710-P-03A-SEAL-ACC', '710-P-03A', 'Condensate Pipeline Booster Pump', 'ISO VG 10', '17.7 L', '10.90 L'),
        ('710-P-03B-SEAL-ACC', '710-P-03B', 'Condensate Pipeline Booster Pump', 'ISO VG 10', '17.7 L', '10.90 L'),
    ]
    
    count = 0
    for acc_id, pump_tag, desc, grade, init_fill, topup in seal_accumulators:
        if acc_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{acc_id}',
    tagNo: '{pump_tag}',
    description: '{desc} Seal System',
    part: 'Accumulator',
    package: 'JI2045-0-PFM108',
    type: LubricantType.OIL,
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '{topup}',
    topUpInterval: '672 hrs (28 Days)',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Two/Three accumulators per mechanical seal; fill quantity is for complete seal system'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} Seal Accumulator")
    
    # ========================================
    # ADDITIONAL FAN MOTORS FOR AIR COMPRESSORS
    # ========================================
    print("[4] إضافة محركات مراوح ضواغط الهواء...")
    
    fan_motors = [
        ('421-EAM-51', '421-EAM-51', 'Intercooler Fan Motor', '421'),
        ('421-EAM-52', '421-EAM-52', 'Aftercooler Fan Motor', '421'),
        ('421-EAM-53', '421-EAM-53', 'Oil Cooler Motor', '421'),
        ('422-EAM-51', '422-EAM-51', 'Intercooler Fan Motor', '422'),
        ('422-EAM-52', '422-EAM-52', 'Aftercooler Fan Motor', '422'),
        ('422-EAM-53', '422-EAM-53', 'Oil Cooler Motor', '422'),
        ('423-EAM-51', '423-EAM-51', 'Intercooler Fan Motor', '423'),
        ('423-EAM-52', '423-EAM-52', 'Aftercooler Fan Motor', '423'),
        ('423-EAM-53', '423-EAM-53', 'Oil Cooler Motor', '423'),
    ]
    
    count = 0
    for motor_id, tag, desc, base_tag in fan_motors:
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '{tag}',
    description: '{desc}',
    part: 'Bearings',
    package: 'JI2045-0-PFM105',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} محرك مروحة")
    
    # ========================================
    # ADDITIONAL CRANES (810-Z-01, 990-Z-01)
    # ========================================
    print("[5] إضافة رافعات إضافية...")
    
    cranes = ['810-Z-01', '990-Z-01']
    count = 0
    
    for crane_tag in cranes:
        crane_name = 'EOT Crane for ' + ('Gas Turbine Generator Building' if '810' in crane_tag else 
                                         'Base Industrielle- Operations Workshop')
        
        crane_parts = [
            (f'{crane_tag}-HOIST', 'Hoist gearbox', 'OIL', 'ISO VG 460', '16 L' if '810' in crane_tag else '16 L', '1.52 L', '8640 hrs', '43200 hrs'),
            (f'{crane_tag}-WIRE', 'Wire rope & rope guide', 'GREASE', 'ISO 2137', '2500 g', '250 g', '4320 hrs', '8640 hrs'),
            (f'{crane_tag}-CT-GB', 'Cross Travel gearbox', 'OIL' if '810' in crane_tag else 'OIL', 'ISO VG 460', '1.5 L', '0.25 L', '8640 hrs', '43200 hrs'),
            (f'{crane_tag}-LT-GB', 'Long Travel gearbox', 'OIL', 'ISO VG 460', '1 L', '0.25 L', '8640 hrs', '43200 hrs'),
        ]
        
        for part_id, part_desc, lub_type, grade, init_fill, topup, topup_int, repl_int in crane_parts:
            if part_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{part_id}',
    tagNo: '{crane_tag}',
    description: '{crane_name}',
    part: '{part_desc}',
    package: 'JI2045-0-PFM113',
    type: LubricantType.{lub_type},
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int}',
    replacementInterval: '{repl_int}',
    brands: {{ bp: 'Energol GR XP460', shell: 'Omala Oil 460', mobil: 'Mobilgear 634', total: 'Carter EP 460', naftal: 'Fodda 460' }},
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  }}''')
                count += 1
        
        # Motor bearings
        for motor_type in ['HOIST', 'CT', 'LT']:
            motor_id = f'{crane_tag}-{motor_type}-MOTOR'
            if motor_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '{crane_tag}',
    description: '{crane_name}',
    part: '{motor_type} Motor Bearings',
    package: 'JI2045-0-PFM113',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
                count += 1
    
    print(f"   ✓ أضيف {count} جزء رافعة")
    
    return new_entries, len(new_entries)

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("إضافة المعدات المفقودة إلى قاعدة البيانات")
    print("="*80)
    print("\nجاري البحث عن المعدات المفقودة وإضافتها...\n")
    
    new_entries, count = generate_additional_equipment()
    
    if count == 0:
        print("\n" + "="*80)
        print("✅ جميع المعدات موجودة بالفعل!")
        print("="*80)
    else:
        # Read current file
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the last entry (before the closing bracket)
        import re
        # Find position of last '];\n'
        match = re.search(r'\n\];\n$', content)
        if match:
            insert_pos = match.start()
            
            # Insert new entries
            new_content = content[:insert_pos] + ',\n' + ',\n'.join(new_entries) + content[insert_pos:]
            
            # Write back
            with open('data.ts', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("\n" + "="*80)
            print("✅ تم بنجاح!")
            print("="*80)
            print(f"\n📊 عدد المعدات المضافة: {count}")
            print(f"📁 تم تحديث الملف: data.ts")
            print("\n" + "="*80)
        else:
            print("\n❌ خطأ: لم يتم العثور على نهاية الملف")
