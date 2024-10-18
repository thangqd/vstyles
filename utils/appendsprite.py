import json
from PIL import Image

def merge_sprites_and_json(sprite_image_1_path, json_1_path, sprite_image_2_path, json_2_path, output_image_path, output_json_path):
    # Open the sprite images
    image1 = Image.open(sprite_image_1_path)
    image2 = Image.open(sprite_image_2_path)

    # Load the JSON files
    with open(json_1_path, 'r') as f1, open(json_2_path, 'r') as f2:
        sprite_json_1 = json.load(f1)
        sprite_json_2 = json.load(f2)

    # Get dimensions of both images
    width1, height1 = image1.size
    width2, height2 = image2.size

    # Create a new image with the combined height (for vertical merge)
    merged_image = Image.new('RGBA', (max(width1, width2), height1 + height2))

    # Paste the two images into the new merged image
    merged_image.paste(image1, (0, 0))
    merged_image.paste(image2, (0, height1))

    # Adjust y values in the second JSON to account for the height of the first image
    for icon in sprite_json_2.values():
        icon['y'] += height1

    # Merge the two JSON objects
    merged_json = {**sprite_json_1, **sprite_json_2}

    # Save the merged image
    merged_image.save(output_image_path)

    # Save the merged JSON
    with open(output_json_path, 'w') as f_out:
        json.dump(merged_json, f_out, indent=4)

    print(f"Merged sprite image saved as {output_image_path}")
    print(f"Merged sprite JSON saved as {output_json_path}")

# Example usage
merge_sprites_and_json(
    sprite_image_1_path='./vstyles/new/sprite.png',
    json_1_path='./vstyles/new/sprite.json',
   
    sprite_image_2_path='./vstyles/esrisprite/sprite.png',
    json_2_path='./vstyles/esrisprite/sprite.json',
   
    output_image_path='./vstyles/topography/sprite.png',
    output_json_path='./vstyles/topography/sprite.json'
)