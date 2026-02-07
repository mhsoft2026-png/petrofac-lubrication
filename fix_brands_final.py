import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Function to convert brands object with multiple others to single 'other' field
def fix_brands_object(brands_obj):
    """Convert brands object with other2, other3, etc. to single 'other' field"""
    # Extract all brand values
    brand_matches = re.findall(r'other\d*: "(.*?)"', brands_obj)
    
    if not brand_matches:
        return '{}'
    
    # Combine all brands into single 'other' field, separated by commas
    combined_brands = ' / '.join(brand_matches)
    return f'{{ other: "{combined_brands}" }}'

# Find all lines with brands objects that have other2, other3, etc.
lines = content.split('\n')
modified = False

for i in range(len(lines)):
    line = lines[i]
    # Check if this line contains brands with other2, other3, etc.
    if 'brands: {' in line and 'other2' in line:
        # Extract the object content
        match = re.search(r'brands: (\{.*?\}),?$', line)
        if match:
            obj_content = match.group(1)
            # Fix the object
            fixed_obj = fix_brands_object(obj_content)
            # Replace in line
            new_line = re.sub(r'brands: \{.*?\},?$', f'brands: {fixed_obj},', line)
            lines[i] = new_line
            modified = True
            print(f"Line {i+1}: Fixed brands object")

if modified:
    # Write back
    content = '\n'.join(lines)
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✅ تم إصلاح جميع أخطاء TypeScript في حقل brands")
    print(f"✅ تم دمج جميع العلامات التجارية في حقل 'other' واحد")
else:
    print("⚠️ لم يتم العثور على أخطاء brands لإصلاحها")
