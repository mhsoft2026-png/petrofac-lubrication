#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to properly add all missing equipment with correct TypeScript syntax
"""

def read_current_data():
    """Read current data.ts and extract existing IDs"""
    try:
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
            import re
            ids = re.findall(r"id: '([^']+)'", content)
            return set(ids), content
    except:
        return set(), ""

def generate_all_missing_equipment():
    """Generate all missing equipment with CORRECT TypeScript syntax"""
    
    existing_ids, current_content = read_current_data()
    
    new_entries = []
    
    print("="*80)
    print("إضافة المعدات المفقودة بصيغة TypeScript صحيحة")
    print("="*80)
    
    # ========================================
    # PUMP MOTORS (38 items)
    # ========================================
    print("\n[1] إضافة محركات المضخات...")
    
    pump_motors = [
        ('401-PM-01A', '401-P-01A', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-01B', '401-P-01B', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-01C', '401-P-01C', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-01D', '401-P-01D', 'Hot Oil Circulation Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-02', '401-P-02', 'Hot Oil Drain Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('401-PM-03', '401-P-03', 'Hot Oil Storage Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('411-PM-01A', '411-P-01A', 'High Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('411-PM-01B', '411-P-01B', 'High Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('412-PM-02A', '412-P-02A', 'Cold Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('412-PM-02B', '412-P-02B', 'Cold Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '6000 hrs (DE) / 6000 hrs (NDE)'),
        ('413-PM-03A', '413-P-03A', 'Low Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('413-PM-03B', '413-P-03B', 'Low Pressure Flare KO Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '7000 hrs (DE) / 7000 hrs (NDE)'),
        ('442-PM-01', '442-P-01', 'Closed Drain Drum Pump Motor', 'NLGI Grade 2', '24 g (DE) / 24 g (NDE)', '5000 hrs (DE) / 5000 hrs (NDE)'),
        ('520-PM-02A', '520-P-02A', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('520-PM-02B', '520-P-02B', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('620-PM-02A', '620-P-02A', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('620-PM-02B', '620-P-02B', 'Deethanizer Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('530-PM-03A', '530-P-03A', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('530-PM-03B', '530-P-03B', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('630-PM-03A', '630-P-03A', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('630-PM-03B', '630-P-03B', 'LPG Product/Reflux Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-04A', '730-P-04A', 'LPG Booster/Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-04B', '730-P-04B', 'LPG Booster/Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('730-PM-04C', '730-P-04C', 'LPG Booster/Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('520-PM-01A', '520-P-01A', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('520-PM-01B', '520-P-01B', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('620-PM-01A', '620-P-01A', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('620-PM-01B', '620-P-01B', 'Wash Column Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-01A', '710-P-01A', 'Condensate Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-01B', '710-P-01B', 'Condensate Pipeline Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-02A', '710-P-02A', 'Off-Spec Condensate Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-02B', '710-P-02B', 'Off-Spec Condensate Return Pump Motor', 'BEM 41-132', '35 g (DE) / 35 g (NDE)', '4000 hrs (DE) / 4000 hrs (NDE)'),
        ('710-PM-03A', '710-P-03A', 'Condensate Pipeline Booster Pump Motor', 'NLGI Grade 2', '34 g (DE) / 34 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
        ('710-PM-03B', '710-P-03B', 'Condensate Pipeline Booster Pump Motor', 'NLGI Grade 2', '34 g (DE) / 34 g (NDE)', '3000 hrs (DE) / 3000 hrs (NDE)'),
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
    # SEAL COOLER MOTORS (21 items)
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
        ('730-P-06-SEAL-MOTOR1', '730-P-06', 'LPG Spiking Pump Seal Cooler Motor 1'),
        ('730-P-06-SEAL-MOTOR2', '730-P-06', 'LPG Spiking Pump Seal Cooler Motor 2'),
        ('730-P-05A-SEAL-MOTOR1', '730-P-05A', 'LPG Pipeline Pump Seal Cooler Motor 1'),
        ('730-P-05A-SEAL-MOTOR2', '730-P-05A', 'LPG Pipeline Pump Seal Cooler Motor 2'),
        ('730-P-05B-SEAL-MOTOR1', '730-P-05B', 'LPG Pipeline Pump Seal Cooler Motor 1'),
        ('730-P-05B-SEAL-MOTOR2', '730-P-05B', 'LPG Pipeline Pump Seal Cooler Motor 2'),
        ('730-P-05C-SEAL-MOTOR1', '730-P-05C', 'LPG Pipeline Pump Seal Cooler Motor 1'),
        ('730-P-05C-SEAL-MOTOR2', '730-P-05C', 'LPG Pipeline Pump Seal Cooler Motor 2'),
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
    # SEAL ACCUMULATORS (25 items)
    # ========================================
    print("[3] إضافة Seal Accumulators...")
    
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
    # AIR COMPRESSOR FAN MOTORS (9 items)
    # ========================================
    print("[4] إضافة محركات مراوح ضواغط الهواء...")
    
    fan_motors = [
        ('421-EAM-51', '421-EAM-51', 'Intercooler Fan Motor'),
        ('421-EAM-52', '421-EAM-52', 'Aftercooler Fan Motor'),
        ('421-EAM-53', '421-EAM-53', 'Oil Cooler Motor'),
        ('422-EAM-51', '422-EAM-51', 'Intercooler Fan Motor'),
        ('422-EAM-52', '422-EAM-52', 'Aftercooler Fan Motor'),
        ('422-EAM-53', '422-EAM-53', 'Oil Cooler Motor'),
        ('423-EAM-51', '423-EAM-51', 'Intercooler Fan Motor'),
        ('423-EAM-52', '423-EAM-52', 'Aftercooler Fan Motor'),
        ('423-EAM-53', '423-EAM-53', 'Oil Cooler Motor'),
    ]
    
    count = 0
    for motor_id, tag, desc in fan_motors:
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
    # ADDITIONAL CRANES (14 items)
    # ========================================
    print("[5] إضافة رافعات إضافية...")
    
    cranes = ['810-Z-01', '990-Z-01']
    count = 0
    
    for crane_tag in cranes:
        crane_name = 'EOT Crane for ' + ('Gas Turbine Generator Building' if '810' in crane_tag else 'Base Industrielle- Operations Workshop')
        
        crane_parts = [
            (f'{crane_tag}-HOIST', 'Hoist gearbox', 'OIL', 'ISO VG 460', '16 L', '1.52 L', '8640 hrs', '43200 hrs'),
            (f'{crane_tag}-WIRE', 'Wire rope & rope guide', 'GREASE', 'ISO 2137', '2500 g', '250 g', '4320 hrs', '8640 hrs'),
            (f'{crane_tag}-CT-GB', 'Cross Travel gearbox', 'OIL', 'ISO VG 460', '1.5 L', '0.25 L', '8640 hrs', '43200 hrs'),
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
    
    # ========================================
    # AIR COOLER MOTORS (38 items - DE & NDE)
    # ========================================
    print("[6] إضافة محركات Air Cooler...")
    
    air_cooler_motors = [
        ('301-EAM-01', 'Feed Gas Compressor After Cooler Motor', '27 g', '4000', '6314-C3'),
        ('302-EAM-01', 'Feed Gas Compressor After Cooler Motor', '27 g', '4000', '6314-C3'),
        ('303-EAM-01', 'Feed Gas Compressor After Cooler Motor', '27 g', '4000', '6314-C3'),
        ('401-EAM-01', 'Hot Oil Trim Cooler Motor', '11 g (DE) / 7 g (NDE)', '14000 (DE) / 17000 (NDE)', '6308-C3 (DE) / 6207-C3 (NDE)'),
        ('510-EAM-01', 'Gas Dehydrator Regeneration Gas Cooler Motor', '13 g (DE) / 9 g (NDE)', '13000 (DE) / 14000 (NDE)', '6309-C3'),
        ('610-EAM-01', 'Gas Dehydrator Regeneration Gas Cooler Motor', '13 g (DE) / 9 g (NDE)', '13000 (DE) / 14000 (NDE)', '6309-C3'),
        ('530-EAM-02', 'LPG Splitter Condenser Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('630-EAM-02', 'LPG Splitter Condenser Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('530-EAM-03', 'Condensate Rundown Cooler Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('630-EAM-03', 'Condensate Rundown Cooler Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('750-EAM-03', 'Sales Gas Compressor After Cooler Motor', '27 g', '4000', '6314-C3'),
        ('751-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', '27 g', '4000', '6314-C3'),
        ('752-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', '27 g', '4000', '6314-C3'),
        ('753-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', '27 g', '4000', '6314-C3'),
        ('754-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', '27 g', '4000', '6314-C3'),
        ('751-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('752-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('753-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('754-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
    ]
    
    count = 0
    for motor_tag, desc, init_fill, repl, bearing in air_cooler_motors:
        if '(DE)' in init_fill or '(NDE)' in init_fill:
            motor_de_id = f'{motor_tag}-DE'
            motor_nde_id = f'{motor_tag}-NDE'
            
            if motor_de_id not in existing_ids:
                de_fill = init_fill.split('/')[0].strip().replace('(DE)', '').strip()
                de_repl = repl.split('/')[0].strip().replace('(DE)', '').strip()
                de_bearing = bearing.split('/')[0].strip().replace('(DE)', '').strip()
                
                new_entries.append(f'''  {{
    id: '{motor_de_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR DRIVE END / {de_bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{de_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{de_repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
            
            if motor_nde_id not in existing_ids:
                nde_fill = init_fill.split('/')[1].strip().replace('(NDE)', '').strip()
                nde_repl = repl.split('/')[1].strip().replace('(NDE)', '').strip()
                nde_bearing = bearing.split('/')[1].strip().replace('(NDE)', '').strip() if '/' in bearing else bearing
                
                new_entries.append(f'''  {{
    id: '{motor_nde_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR NON DRIVE END / {nde_bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{nde_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{nde_repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
        else:
            motor_de_id = f'{motor_tag}-DE'
            motor_nde_id = f'{motor_tag}-NDE'
            
            if motor_de_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{motor_de_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR DRIVE END / {bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{init_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
            
            if motor_nde_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{motor_nde_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR NON DRIVE END / {bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{init_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
    
    print(f"   ✓ أضيف {count} محرك Air Cooler")
    
    return new_entries, len(new_entries)

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("إضافة جميع المعدات المفقودة")
    print("="*80)
    print("\nجاري الإضافة...\n")
    
    new_entries, count = generate_all_missing_equipment()
    
    if count == 0:
        print("\n" + "="*80)
        print("✅ جميع المعدات موجودة بالفعل!")
        print("="*80)
    else:
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
        
        import re
        match = re.search(r'\n\];\n$', content)
        if match:
            insert_pos = match.start()
            new_content = content[:insert_pos] + ',\n' + ',\n'.join(new_entries) + content[insert_pos:]
            
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
