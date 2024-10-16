
import json
from PIL import Image

def append_sprite_and_json_vertically(existing_sprite_path, new_sprite_path, existing_json_path, output_sprite_path, output_json_path, new_sprite_name):
    # Open the existing sprite sheet and the new sprite image
    existing_sprite = Image.open(existing_sprite_path)
    new_sprite = Image.open(new_sprite_path)
    
    # Load existing JSON data
    with open(existing_json_path, 'r') as f:
        sprite_json = json.load(f)
    
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
    
    # Calculate the position of the new sprite in the sheet
    new_sprite_position = {"x": 0, "y": height_existing, "w": width_new, "h": height_new}
    
    # Add new sprite's data to the JSON
    sprite_json[new_sprite_name] = {
        "frame": new_sprite_position
    }
    
    # Save the updated sprite sheet
    new_sprite_sheet.save(output_sprite_path)
    
    # Save the updated JSON file
    with open(output_json_path, 'w') as f:
        json.dump(sprite_json, f, indent=4)

# Example usage
append_sprite_and_json_vertically(
    existing_sprite_path='./vstyles/bright/sprite@2x.png',
    new_sprite_path='./vstyles/topography/sprite@2x.png',
    existing_json_path='./vstyles/bright/sprite@2x.json',
   
    output_sprite_path='./vstyles/topography/newsprite@2x.png',
    output_json_path='./vstyles/topography/newsprite@2x.json',
    new_sprite_name='newsprite'
)
