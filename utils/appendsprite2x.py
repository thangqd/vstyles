import json
from PIL import Image

def append_sprite_and_json_vertically(existing_sprite_path, new_sprite_path, existing_json_path, new_json_path, output_sprite_path, output_json_path, new_sprite_name):
    # Open the existing sprite sheet and the new sprite image
    existing_sprite = Image.open(existing_sprite_path)
    new_sprite = Image.open(new_sprite_path)
    
    # Load existing JSON data
    with open(existing_json_path, 'r') as f:
        existing_sprite_json = json.load(f)
    
    # Load the new JSON data (for the new sprite)
    with open(new_json_path, 'r') as f:
        new_sprite_json = json.load(f)
    
    # Get dimensions of both images
    width_existing, height_existing = existing_sprite.size
    width_new, height_new = new_sprite.size
    
    # Calculate the new dimensions for the sprite sheet (vertical append)
    total_width = max(width_existing, width_new)
    total_height = height_existing + height_new
    new_sprite_sheet = Image.new('RGBA', (total_width, total_height))
    
    # Paste existing sprite at the top
    new_sprite_sheet.paste(existing_sprite, (0, 0))
    
    # Paste new sprite below the existing one
    new_sprite_sheet.paste(new_sprite, (0, height_existing))
    
    # Update new sprite's JSON data to reflect the new position
    for sprite_name, sprite_data in new_sprite_json.items():
        # Update the `x` and `y` positions for the new sprite
        sprite_data['x'] = 0  # Align with the left side (x = 0)
        sprite_data['y'] = height_existing  # Position below the existing sprite
        new_sprite_json[sprite_name] = sprite_data
        
        # Add the new sprite's JSON data to the existing JSON
        existing_sprite_json[sprite_name] = sprite_data

    # Save the updated sprite sheet
    new_sprite_sheet.save(output_sprite_path)
    
    # Save the updated JSON file
    with open(output_json_path, 'w') as f:
        json.dump(existing_sprite_json, f, indent=4)

# Example usage
append_sprite_and_json_vertically(
    existing_sprite_path='./vstyles/topo_backup/sprite@2x.png',
    new_sprite_path='./vstyles/vnsprite/sprite@2x.png',
   
    existing_json_path='./vstyles/topo_backup/sprite@2x.json',
    new_json_path='./vstyles/vnsprite/sprite@2x.json',
   
    output_sprite_path='./vstyles/topography/sprite@2x.png',
    output_json_path='./vstyles/topography/sprite@2x.json',

    new_sprite_name='vsprite'
)