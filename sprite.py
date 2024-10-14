from PIL import Image
import json

# Load the sprite.json
with open('sprite.json') as f:
    sprite_data = json.load(f)

# Load the sprite.png
sprite_image = Image.open('sprite.png')

# Function to extract a sprite
def extract_sprite(sprite_name):
    # Check if the sprite name exists in the JSON
    if sprite_name in sprite_data:
        sprite_info = sprite_data[sprite_name]
        
        # Extract the x, y, width, and height
        x = sprite_info['x']
        y = sprite_info['y']
        width = sprite_info['width']
        height = sprite_info['height']

        # Crop the sprite from the sprite.png
        sprite_cropped = sprite_image.crop((x, y, x + width, y + height))
        
        # Save or display the cropped sprite
        sprite_cropped.save(f'depresion.png')
        print(f'Sprite "{sprite_name}" extracted and saved as "{sprite_name}.png".')
    else:
        print(f'Sprite "{sprite_name}" not found in sprite.json.')

# Example usage
extract_sprite("Depression/0")
