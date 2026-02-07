import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Function to convert brands array to object format
def convert_brands_to_object(brands_array):
    """Convert brands array to object format"""
    # Remove brackets and split by comma
    brands_str = brands_array.strip("[]'\"")
    brands_list = [b.strip().strip("'\"") for b in brands_str.split("', '")]
    
    if brands_list == ['-'] or brands_list == ['']:
        return '{}'
    
    # Create object with 'other' key for each brand
    brands_obj_parts = []
    for i, brand in enumerate(brands_list):
        if brand and brand != '-':
            key = f'other{i+1}' if i > 0 else 'other'
            brands_obj_parts.append(f'{key}: "{brand}"')
    
    if brands_obj_parts:
        return '{ ' + ', '.join(brands_obj_parts) + ' }'
    return '{}'

# Find all lines with brands as arrays (starting from line 11000 onwards)
lines = content.split('\n')
modified = False

for i in range(len(lines)):
    line = lines[i]
    # Check if this line contains brands with array format
    if 'brands: [' in line and i > 11000:
        # Extract the array content
        match = re.search(r"brands: (\[.*?\]),?$", line)
        if match:
            array_content = match.group(1)
            # Convert to object
            obj_content = convert_brands_to_object(array_content)
            # Replace in line
            new_line = re.sub(r'brands: \[.*?\],?$', f'brands: {obj_content},', line)
            lines[i] = new_line
            modified = True
            print(f"Line {i+1}: Converted brands from array to object")

if modified:
    # Write back
    content = '\n'.join(lines)
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✅ تم إصلاح أخطاء TypeScript في حقل brands")
else:
    print("⚠️ لم يتم العثور على أخطاء brands لإصلاحها")
