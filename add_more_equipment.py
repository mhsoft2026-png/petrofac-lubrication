#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add MORE missing equipment from PDF
Including: GTG Package, Diesel Engine, Standalone Pumps, Waste Oil, etc.
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

def generate_more_equipment():
    """Generate all additional missing equipment"""
    
    existing_ids, current_content = read_current_data()
    
    new_entries = []
    
    print("="*80)
    print("إضافة معدات إضافية من PDF")
    print("="*80)
    
    # ========================================
    # GTG PACKAGE EQUIPMENT (811/812/813/814/815)
    # ========================================
    print("\n[1] إضافة معدات حزم GTG...")
    
    gtg_units = ['811', '812', '813', '814', '815']
    count = 0
    
    # Ratchet Pumps (811/812/813/814/815-P-05)
    for unit in gtg_units:
        pump_id = f'{unit}-P-05'
        if pump_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{pump_id}',
    tagNo: '{pump_id}',
    description: 'Ratchet Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Self lubricated by pumped fluid'
  }}''')
            count += 1
        
        # Ratchet Pump Motor
        motor_id = f'{unit}-PM-05'
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '{motor_id}',
    description: 'Ratchet Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
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
        
        # Hydraulic Oil Main Pump
        hyd_pump_id = f'{unit}-P-04'
        if hyd_pump_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{hyd_pump_id}',
    tagNo: '{hyd_pump_id}',
    description: 'Hydraulic Oil Main Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Self lubricated by pumped fluid'
  }}''')
            count += 1
        
        # Lube Oil Cooler Fans (A/B/C)
        for fan_suffix in ['A', 'B', 'C']:
            fan_id = f'{unit}-EAF-01{fan_suffix}'
            if fan_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{fan_id}',
    tagNo: '{fan_id}',
    description: 'Lube Oil Cooler Fan',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '140 g',
    topUpQty: '70 g (Upper) / 70 g (Lower)',
    topUpInterval: '3000 hrs',
    replacementInterval: '3000 hrs',
    brands: {{ bp: 'Olista Longtime 3EP', shell: 'Alvina EP', mobil: 'Unirex N2 or N3', naftal: 'AGIP - GR MU EP2' }},
    remarks: 'Grease shall be Lithium Complex Base'
  }}''')
                count += 1
            
            # Lube Oil Cooler Fan Motors
            fan_motor_id = f'{unit}-EAM-01{fan_suffix}'
            if fan_motor_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{fan_motor_id}',
    tagNo: '{fan_motor_id}',
    description: 'Lube Oil Cooler Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '100 g',
    topUpQty: '50 g (DE) / 50 g (NDE)',
    topUpInterval: '3000 hrs',
    replacementInterval: '3000 hrs',
    brands: {{ shell: 'GADUS S5 V 100 2', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A', other: 'KLUBERPLEX BEM 41-132' }},
    remarks: 'Grease shall be Lithium Complex Base'
  }}''')
                count += 1
        
        # Charge Pump For Torque Convertor
        charge_pump_id = f'{unit}-P-06'
        if charge_pump_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{charge_pump_id}',
    tagNo: '{charge_pump_id}',
    description: 'Charge Pump For Torque Convertor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Self lubricated by pumped fluid'
  }}''')
            count += 1
        
        # Starting Motor
        start_motor_id = f'{unit}-PM-06'
        if start_motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{start_motor_id}',
    tagNo: '{start_motor_id}',
    description: 'Starting Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '65 g',
    topUpQty: '41 g (DE) / 24 g (NDE)',
    topUpInterval: '1000 hrs (NDE) / 1400 hrs (DE)',
    replacementInterval: '1000 hrs (NDE) / 1400 hrs (DE)',
    brands: {{ mobil: 'Polyrex EM' }},
    remarks: 'Grease shall be Lithium Complex Base. Initial Fill at Factory'
  }}''')
            count += 1
        
        # Dust Extractor Fan Motors
        for fan_num in ['03', '04']:
            dust_fan_id = f'{unit}-KM-{fan_num}'
            if dust_fan_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{dust_fan_id}',
    tagNo: '{dust_fan_id}',
    description: 'Dust Extractor Fan Motor',
    part: 'Sealed Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Lubrication not required. Bearings L10 rating life 40000 hrs'
  }}''')
                count += 1
        
        # Main and Auxiliary Ventilation Fan Motors
        for vent_suffix in ['A', 'B']:
            vent_motor_id = f'{unit}-KM-01{vent_suffix}'
            if vent_motor_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{vent_motor_id}',
    tagNo: '{vent_motor_id}',
    description: 'Main and Auxiliary Ventilation Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '80 g',
    topUpQty: '40 g (DE) / 40 g (NDE)',
    topUpInterval: '7800 hrs',
    replacementInterval: '7800 hrs',
    brands: {{ mobil: 'Unirex N2 or N3' }},
    remarks: 'Grease shall be Lithium Complex Base. Initial Fill at Factory'
  }}''')
                count += 1
        
        # Generator Cooler Fan Motors
        for gen_suffix in ['A', 'B', 'C']:
            gen_motor_id = f'{unit}-GEM-01{gen_suffix}'
            if gen_motor_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{gen_motor_id}',
    tagNo: '{gen_motor_id}',
    description: 'Generator Cooler Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
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
        
        # Gas Turbine Generator
        gtg_id = f'{unit}-GT-01'
        if gtg_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{gtg_id}',
    tagNo: '{gtg_id}',
    description: 'Gas Turbine Generator',
    part: 'Washing Detergent',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: 'BH ITN07831.04 AND GEI 41042p',
    initialFill: '600 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '200 litres of detergent is required for one off-line washing cycle of one GTG Unit'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} قطعة من معدات GTG")
    
    # ========================================
    # WASHING SOLUTION PUMP (810)
    # ========================================
    print("[2] إضافة مضخة محلول الغسيل...")
    
    wash_items = [
        ('810-P-07', 'Washing Solution Pump', 'Bearings', '-', '-', '-', '-'),
        ('810-PM-07', 'Washing Solution Pump Motor', 'Bearings', '-', '-', '-', '-'),
    ]
    
    count = 0
    for item_id, desc, part, grade, init, topup, repl in wash_items:
        if item_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{item_id}',
    tagNo: '{item_id}',
    description: '{desc}',
    part: '{part}',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '{grade}',
    initialFill: '{init}',
    topUpQty: '{topup}',
    topUpInterval: '{repl}',
    replacementInterval: '{repl}',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} مضخة غسيل")
    
    # ========================================
    # DIESEL ENGINE & GENERATOR (830)
    # ========================================
    print("[3] إضافة محرك الديزل والمولد...")
    
    count = 0
    
    # Diesel Engine
    diesel_id = '830-GD-01-LUB'
    if diesel_id not in existing_ids:
        new_entries.append(f'''  {{
    id: '{diesel_id}',
    tagNo: '830-GD-01',
    description: 'Diesel Engine',
    part: 'Lubrication System',
    package: 'MAI-LST-830-46852',
    type: LubricantType.OIL,
    grade: '20W40 CH4',
    initialFill: '1136 L',
    topUpQty: 'Refer Remark-1',
    topUpInterval: 'Refer Remark-1',
    replacementInterval: '2000 hrs',
    brands: {{ bp: 'VISCO 2000', shell: 'RIMULA', mobil: 'DELVAC', total: 'RUBIA', naftal: 'CHELIA TD 20W40' }},
    remarks: '1. Oil consumption shall be 1.9 litres/hour. Top-up determined accordingly. 2. Based on Operating hours'
  }}''')
        count += 1
    
    # Diesel Engine Cooling System
    diesel_cool_id = '830-GD-01-COOL'
    if diesel_cool_id not in existing_ids:
        new_entries.append(f'''  {{
    id: '{diesel_cool_id}',
    tagNo: '830-GD-01',
    description: 'Diesel Engine',
    part: 'Cooling System',
    package: 'MAI-LST-830-46852',
    type: LubricantType.OIL,
    grade: 'ASTM D3306 (50% Mono Ethylene Glycol + 50% Potable Water)',
    initialFill: '1200 L',
    topUpQty: 'Refer Remark-1',
    topUpInterval: 'Refer Remark-1',
    replacementInterval: 'Refer Remark-1',
    brands: {{ shell: 'ROTELLA', mobil: 'HEAVY DUTY', total: 'COOLELF' }},
    remarks: 'Coolant used in closed loop. Top-up for leakage during maintenance. First Fill by EDG Vendor'
  }}''')
        count += 1
    
    # Generator
    gen_id = '830-GE-01'
    if gen_id not in existing_ids:
        new_entries.append(f'''  {{
    id: '{gen_id}',
    tagNo: '{gen_id}',
    description: 'Generator',
    part: 'Bearings',
    package: 'MAI-LST-830-46852',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '80 g (DE) / 70 g (NDE)',
    topUpQty: '30 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'GADUS S2 V220 2', mobil: 'Mobilux EP2', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        count += 1
    
    # Engine for Air Compressor
    eng_comp_id = '830-KD-52'
    if eng_comp_id not in existing_ids:
        new_entries.append(f'''  {{
    id: '{eng_comp_id}',
    tagNo: '{eng_comp_id}',
    description: 'Engine for Air Compressor (830-K-52)',
    part: 'Lubrication System',
    package: 'MAI-LST-830-46852',
    type: LubricantType.OIL,
    grade: '20W40 CH4',
    initialFill: '1.5 L',
    topUpQty: 'Refer Remark-1',
    topUpInterval: 'Refer Remark-1',
    replacementInterval: '250 hrs or 8640 hrs',
    brands: {{ bp: 'VISCO 2000', shell: 'RIMULA', mobil: 'DELVAC', total: 'RUBIA', naftal: 'CHELIA TD 20W40' }},
    remarks: 'Diesel Compressor is standby equipment. Top-up as required'
  }}''')
        count += 1
    
    # Air Compressors (830-K-51/52)
    for comp_num in ['51', '52']:
        comp_id = f'830-K-{comp_num}'
        if comp_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{comp_id}',
    tagNo: '{comp_id}',
    description: 'Air Compressor',
    part: 'Bearings',
    package: 'MAI-LST-830-46852',
    type: LubricantType.OIL,
    grade: 'SAE 30 HD',
    initialFill: '3 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '400 hrs or 8640 hrs (first oil change in 50 working hours)',
    brands: {{ shell: 'HELIX', mobil: 'MOBILTRANS', total: 'RUBIA FLEET' }},
    remarks: ''
  }}''')
            count += 1
    
    # Motor for Air Compressor
    comp_motor_id = '830-KM-51'
    if comp_motor_id not in existing_ids:
        new_entries.append(f'''  {{
    id: '{comp_motor_id}',
    tagNo: '{comp_motor_id}',
    description: 'Motor for Air Compressor (830-K-51)',
    part: 'Bearings',
    package: 'MAI-LST-830-46852',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '30 g (DE) / 30 g (NDE)',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '8640 hrs',
    brands: {{ mobil: 'UNIREX N2/3' }},
    remarks: ''
  }}''')
        count += 1
    
    # Radiator Electrofans
    for fan_num in ['51', '52', '53', '54', '55', '56']:
        fan_id = f'830-EAM-{fan_num}'
        if fan_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{fan_id}',
    tagNo: '{fan_id}',
    description: 'Radiator Electrofan',
    part: 'Bearings',
    package: 'MAI-LST-830-46852',
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
    
    # Container Electrofans
    for fan_num in ['53', '54', '55']:
        cont_fan_id = f'830-KM-{fan_num}'
        if cont_fan_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{cont_fan_id}',
    tagNo: '{cont_fan_id}',
    description: 'Container Electrofan',
    part: 'Bearings',
    package: 'MAI-LST-830-46852',
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
    
    print(f"   ✓ أضيف {count} قطعة محرك ديزل ومولد")
    
    # ========================================
    # CENTRIFUGAL NON-API PUMPS
    # ========================================
    print("[4] إضافة مضخات Centrifugal...")
    
    centrifugal_pumps = [
        # Raw Water Pumps
        ('431-P-01A', 'Raw Water Pump', 'Bearings', 'ISO VG32 or ISO VG46', '1 L', '4000 hrs'),
        ('431-P-01B', 'Raw Water Pump', 'Bearings', 'ISO VG32 or ISO VG46', '1 L', '4000 hrs'),
        ('431-PM-01A', 'Raw Water Pump Motor', 'Bearings', 'NLGI Grade 2', '13 g (DE) / 9 g (NDE)', '11000 (DE) / 13000 (NDE)'),
        ('431-PM-01B', 'Raw Water Pump Motor', 'Bearings', 'NLGI Grade 2', '13 g (DE) / 9 g (NDE)', '11000 (DE) / 13000 (NDE)'),
        # Diesel Storage Pump
        ('472-P-01', 'Diesel Storage Pump', 'Bearings', 'ISO VG32 or ISO VG46', '0.5 L', '4000 hrs'),
        ('472-PM-01', 'Diesel Storage Pump Motor', 'Bearings', 'NLGI Grade 2', '11 g (DE) / 7 g (NDE)', '13000 (DE) / 16000 (NDE)'),
        # Potable Water Pumps
        ('432-P-11A', 'Potable Water Pump', 'Bearings', 'ISO VG32 or ISO VG46', '1 L', '4000 hrs'),
        ('432-P-11B', 'Potable Water Pump', 'Bearings', 'ISO VG32 or ISO VG46', '1 L', '4000 hrs'),
        ('432-PM-11A', 'Potable Water Pump Motor', 'Bearings', 'NLGI Grade 2', '13 g (DE) / 9 g (NDE)', '11000 (DE) / 13000 (NDE)'),
        ('432-PM-11B', 'Potable Water Pump Motor', 'Bearings', 'NLGI Grade 2', '13 g (DE) / 9 g (NDE)', '11000 (DE) / 13000 (NDE)'),
    ]
    
    count = 0
    for pump_id, desc, part, grade, init_fill, repl in centrifugal_pumps:
        if pump_id not in existing_ids:
            lub_type = 'OIL' if 'VG' in grade else 'GREASE'
            brands = {}
            if lub_type == 'OIL':
                brands = '{ bp: "ENERGOL HL32/HL46", shell: "TELLUS 32/01 C 46", mobil: "MOBIL DTE 24/25", total: "Azolla ZS 32/46", naftal: "TISKA 32/46" }'
            else:
                brands = '{ bp: "ENER LS2", shell: "GADUS S2 V220 2", mobil: "POLYREX EM", total: "MULTIS EP2", naftal: "TESSALA EP2" }'
            
            new_entries.append(f'''  {{
    id: '{pump_id}',
    tagNo: '{pump_id}',
    description: '{desc}',
    part: '{part}',
    package: 'JI2045-0-PFM117',
    type: LubricantType.{lub_type},
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{repl}',
    brands: {brands},
    remarks: 'First oil change in 300 hours' if lub_type == 'OIL' else ''
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} مضخة Centrifugal")
    
    # ========================================
    # FIRE WATER PUMPS
    # ========================================
    print("[5] إضافة مضخات مكافحة الحريق...")
    
    fire_pumps = [
        ('450-P-02A', 'Fire Water Pump (Motor Driven)', 'Bearing', 'NLGI Grade 2', '100 g', '50 g', '4320', '8640'),
        ('450-P-02B', 'Fire Water Pump (Motor Driven)', 'Bearing', 'NLGI Grade 2', '100 g', '50 g', '4320', '8640'),
        ('450-PM-02A', 'Fire Water Pump Motor', 'Bearing', 'NLGI Grade 2', '105 g', '50 g', '4320', '8640'),
        ('450-PM-02B', 'Fire Water Pump Motor', 'Bearing', 'NLGI Grade 2', '105 g', '50 g', '4320', '8640'),
        ('450-P-03A', 'Fire Water Pump (Diesel Engine Driven)', 'Bearing', 'NLGI Grade 2', '100 g', '50 g', '4320', '8640'),
        ('450-P-03B', 'Fire Water Pump (Diesel Engine Driven)', 'Bearing', 'NLGI Grade 2', '100 g', '50 g', '4320', '8640'),
        ('450-P-01A', 'Fire Water Jockey Pump', 'Bearing', 'ISO VG 46', '1.1 L', '0.20 L', '4320', '8640'),
        ('450-P-01B', 'Fire Water Jockey Pump', 'Bearing', 'ISO VG 46', '1.1 L', '0.20 L', '4320', '8640'),
        ('450-PM-01A', 'Fire Water Jockey Pump Motor', 'Bearing', 'NLGI Grade 2', '70 g', '30 g', '4320', '8640'),
        ('450-PM-01B', 'Fire Water Jockey Pump Motor', 'Bearing', 'NLGI Grade 2', '70 g', '30 g', '4320', '8640'),
    ]
    
    count = 0
    for pump_id, desc, part, grade, init_fill, topup, topup_int, repl in fire_pumps:
        if pump_id not in existing_ids:
            lub_type = 'OIL' if 'VG' in grade else 'GREASE'
            brands = {}
            if lub_type == 'OIL':
                brands = '{ bp: "ENERGOL HPL-D-46", shell: "TELLUS S46", mobil: "DTE 25", total: "EQUIVIS ZS 46", naftal: "TISKA 46" }'
            else:
                brands = '{ bp: "ENER LS2", shell: "GADUS S2 V220 2", mobil: "Mobilux EP2", total: "MULTIS EP2", naftal: "TESSALA EP2" }'
            
            new_entries.append(f'''  {{
    id: '{pump_id}',
    tagNo: '{pump_id}',
    description: '{desc}',
    part: '{part}',
    package: 'C-MAI-LST-460-47452',
    type: LubricantType.{lub_type},
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int} hrs',
    replacementInterval: '{repl} hrs',
    brands: {brands},
    remarks: ''
  }}''')
            count += 1
    
    # Fire Water Pump Diesel Engines
    for engine_suffix in ['A', 'B']:
        # Oil Pan
        engine_oil_id = f'450-PD-03{engine_suffix}-OIL'
        if engine_oil_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{engine_oil_id}',
    tagNo: '450-PD-03{engine_suffix}',
    description: 'Fire Water Pump Diesel Engine',
    part: 'Oil Pan',
    package: 'C-MAI-LST-460-47452',
    type: LubricantType.OIL,
    grade: 'SAE 15W-40 API CJ-4 / CK-4',
    initialFill: '45 L',
    topUpQty: '8 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: {{ bp: 'BP VANELLUS MULTI-FLEET', shell: 'Rotella T5', mobil: 'Delvac', total: 'RUBIA TIR 7400', naftal: 'CHEVIA VP SUPER DIESEL' }},
    remarks: 'CUMMINS RECOMMENDS VALVOLINE PREMIUM BLUE'
  }}''')
            count += 1
        
        # Heat Exchanger
        engine_cool_id = f'450-PD-03{engine_suffix}-COOL'
        if engine_cool_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{engine_cool_id}',
    tagNo: '450-PD-03{engine_suffix}',
    description: 'Fire Water Pump Diesel Engine',
    part: 'Heat Exchanger (Engine Coolant)',
    package: 'C-MAI-LST-460-47452',
    type: LubricantType.OIL,
    grade: 'ASTM D6210 (50%Glycol+50%Potable Water)',
    initialFill: '52.6 L',
    topUpQty: '15 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: {{}},
    remarks: ''
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} مضخة مكافحة حريق")
    
    # ========================================
    # WASTE OIL SYSTEM (441)
    # ========================================
    print("[6] إضافة نظام الزيت المستعمل...")
    
    waste_oil_items = [
        ('414-P-04A', 'Disposal Flare Pump', 'Pump Drive End', 'OIL', 'ISO VG 220', '0.95 L', '0.95 L', '4320', '4320'),
        ('414-P-04B', 'Disposal Flare Pump', 'Pump Drive End', 'OIL', 'ISO VG 220', '0.95 L', '0.95 L', '4320', '4320'),
        ('414-P-04A-DRDS', 'Disposal Flare Pump', 'Pump DRDS Oil', 'OIL', 'ISO VG 220', '0.05 L', '0.05 L', '-', '-'),
        ('414-P-04B-DRDS', 'Disposal Flare Pump', 'Pump DRDS Oil', 'OIL', 'ISO VG 220', '0.05 L', '0.05 L', '-', '-'),
        ('414-P-04A-MOTOR', 'Disposal Flare Pump', 'Pump Motor-Bearing', 'GREASE', 'NLGI-2', '-', '-', '-', '-'),
        ('414-P-04B-MOTOR', 'Disposal Flare Pump', 'Pump Motor-Bearing', 'GREASE', 'NLGI-2', '-', '-', '-', '-'),
        ('411-EAM-501-MOTOR', 'Winch', 'Winch motor', 'GREASE', 'NLGI-2', '-', '-', '-', '-'),
        ('411-EAM-501-GEAR', 'Winch', 'Gear reducer', 'OIL', 'ISO VG 680', '4.25 L', '4.25 L', '4320', '25920'),
        ('441-P-03A-JOINT', 'Waste Oil Pump', 'Pump Joint', 'OIL', 'ISO VG 460', '0.01 L', '-', '-', '4000'),
        ('441-P-03A-GEAR', 'Waste Oil Pump', 'Gear Unit', 'OIL', 'CLP VG 220', '0.65 L', '-', '-', '10000'),
        ('441-P-03B-JOINT', 'Waste Oil Pump', 'Pump Joint', 'OIL', 'ISO VG 460', '0.01 L', '-', '-', '4000'),
        ('441-P-03B-GEAR', 'Waste Oil Pump', 'Gear Unit', 'OIL', 'CLP VG 220', '0.65 L', '-', '-', '10000'),
        ('441-M-51', 'Recovered Oil Pit Mixer', 'Reducer', 'OIL', 'ISO VG 220', '3.9 L', '-', '-', '10000'),
        ('441-M-52', 'Inlet Mixing Chamber Mixer', 'Reducer', 'OIL', 'ISO VG 220', '3.9 L', '-', '-', '10000'),
    ]
    
    count = 0
    for item_id, desc, part, lub_type_str, grade, init, topup, topup_int, repl in waste_oil_items:
        if item_id not in existing_ids:
            remarks = 'Greased For Life' if grade == 'NLGI-2' and init == '-' else '1st fill by package vendor'
            brands = '{}' if remarks == 'Greased For Life' else '{ mobil: "Mobilgear 600 XP 220" }'
            
            new_entries.append(f'''  {{
    id: '{item_id}',
    tagNo: '{item_id.split("-")[0]}-{item_id.split("-")[1]}-{item_id.split("-")[2][:2]}{"".join([c for c in item_id.split("-")[2] if c.isalpha()])}',
    description: '{desc}',
    part: '{part}',
    package: 'JI2045-5-PFM002',
    type: LubricantType.{lub_type_str},
    grade: '{grade}',
    initialFill: '{init}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int} hrs' if topup_int != '-' else '-',
    replacementInterval: '{repl} hrs' if repl != '-' else '-',
    brands: {brands},
    remarks: '{remarks}'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} قطعة نظام زيت مستعمل")
    
    # ========================================
    # AVIATION FUEL SYSTEM (471)
    # ========================================
    print("[7] إضافة نظام وقود الطيران...")
    
    aviation_items = [
        ('471-PK-01', 'Air Lubricator', 'Air Lubricator', 'OIL', 'ISO VG 32', '0.05 L', '0.02 L', 'Refer Remark', '-'),
        ('471-GR-GB1', 'GR Pump Gearbox', 'Gearbox', 'OIL', 'SAE 90 ISO 220', '0.6 L', '-', 'Refer Remark', '-'),
        ('471-GR-GB2', 'GR Pump Gearbox', 'Oil Dispersant', 'OIL', 'Molykote M55', '0.06 L', '-', 'Refer Remark', '-'),
        ('471-AIR-COMP', 'Air Compressor', 'Compressor', 'OIL', 'SAE 30-40 ISO 100', '0.5 L', '0.10 L', 'Refer Remark', '-'),
        ('471-HYD-TANK', 'Hydraulic Tank', 'Tank', 'OIL', 'ISO VG 68', '100 L', '-', 'Refer Remark', '-'),
    ]
    
    count = 0
    for item_id, desc, part, lub_type_str, grade, init, topup, topup_int, repl in aviation_items:
        if item_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{item_id}',
    tagNo: '{item_id}',
    description: '{desc}',
    part: '{part}',
    package: 'R-MAI-LST-471-48202',
    type: LubricantType.{lub_type_str},
    grade: '{grade}',
    initialFill: '{init}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int}',
    replacementInterval: '{repl}',
    brands: {{}},
    remarks: 'Keep filled with lube. Top-Up Frequency depends on losses. Supplied by Vendor'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} قطعة نظام وقود طيران")
    
    # ========================================
    # CRANE 990-Z-02 (Missing)
    # ========================================
    print("[8] إضافة رافعة 990-Z-02...")
    
    crane_990_02_parts = [
        ('990-Z-02-HOIST', 'Hoist gearbox', 'OIL', 'ISO VG 460', '16 L', '1.52 L', '8640', '43200'),
        ('990-Z-02-WIRE', 'Wire rope & rope guide', 'GREASE', 'ISO 2137', '2500 g', '250 g', '4320', '8640'),
        ('990-Z-02-CT-GB', 'Cross Travel gearbox', 'OIL', 'ISO VG 460', '1.5 L', '0.25 L', '8640', '43200'),
        ('990-Z-02-LT-GB', 'Long Travel gearbox', 'OIL', 'ISO VG 460', '1 L', '0.25 L', '8640', '43200'),
        ('990-Z-02-SPLINE', 'Spline shaft cross travel', 'GREASE', 'ISO 2137', '200 g', '-', '-', '43200'),
        ('990-Z-02-SPRINGS', 'Springs on overload cut off', 'GREASE', 'ISO 2137', '50 g', '50 g', '8640', '8640'),
    ]
    
    count = 0
    for part_id, part_desc, lub_type_str, grade, init, topup, topup_int, repl in crane_990_02_parts:
        if part_id not in existing_ids:
            brands = '{ bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" }' if lub_type_str == 'OIL' else '{ bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" }'
            
            new_entries.append(f'''  {{
    id: '{part_id}',
    tagNo: '990-Z-02',
    description: 'EOT Crane for Base Industrielle Well Engineering Workshop',
    part: '{part_desc}',
    package: 'JI2045-0-PFM113',
    type: LubricantType.{lub_type_str},
    grade: '{grade}',
    initialFill: '{init}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int} hrs' if topup_int != '-' else '-',
    replacementInterval: '{repl} hrs',
    brands: {brands},
    remarks: 'Replace at overhaul. Initial fill by package vendor'
  }}''')
            count += 1
    
    # Motor bearings for 990-Z-02
    for motor_type in ['HOIST', 'CT', 'LT']:
        motor_id = f'990-Z-02-{motor_type}-MOTOR'
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '990-Z-02',
    description: 'EOT Crane for Base Industrielle Well Engineering Workshop',
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
    
    print(f"   ✓ أضيف {count} قطعة رافعة")
    
    return new_entries, len(new_entries)

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("إضافة معدات إضافية شاملة من ملف PDF")
    print("="*80)
    print("\nجاري البحث والإضافة...\n")
    
    new_entries, count = generate_more_equipment()
    
    if count == 0:
        print("\n" + "="*80)
        print("✅ جميع المعدات موجودة بالفعل!")
        print("="*80)
    else:
        # Read current file
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find position
        import re
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
