import json
from PIL import Image

def append_sprite_and_json_vertically(existing_sprite_path, new_sprite_path, existing_json_path, new_json_path, output_sprite_path, output_json_path, new_sprite_name):
    """
    Appends a new sprite image and its JSON data vertically to an existing sprite sheet.
    """
    try:
        # Open the existing sprite sheet and the new sprite image
        existing_sprite = Image.open(existing_sprite_path)
        new_sprite = Image.open(new_sprite_path)
    except Exception as e:
        print(f"Error opening image files: {e}")
        return

    try:
        # Load existing JSON data
        with open(existing_json_path, 'r') as f:
            existing_sprite_json = json.load(f)
        
        # Load the new JSON data
        with open(new_json_path, 'r') as f:
            new_sprite_json = json.load(f)
    except Exception as e:
        print(f"Error loading JSON files: {e}")
        return

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
    
    # Start y position below the existing sprites
    current_y = height_existing

    # Update new sprite's JSON data to reflect the new position
    for sprite_name, sprite_data in new_sprite_json.items():
        # Update the `x` position for all new sprites to align with the left side (x = 0)
        sprite_data['x'] = 0
        
        # Update the `y` position based on current_y
        sprite_data['y'] = current_y
        
        # Add the new sprite's JSON data to the existing JSON
        existing_sprite_json[sprite_name] = sprite_data
        
        # Increment current_y by the height of the new sprite for the next one
        current_y += sprite_data['height']  # Assuming all new sprites have the same height

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