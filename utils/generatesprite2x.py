from PIL import Image
import os
import json

def create_sprite_from_folder(folder_path, output_image_path, json_output_path, images_per_row=3, padding=0, valid_extensions=('png', 'jpg', 'jpeg')):
    # List all image files in the folder with valid extensions
    image_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                  if f.lower().endswith(valid_extensions)]
    
    if not image_list:
        print("No images found in the folder.")
        return

    # Open all images
    images = [Image.open(img) for img in image_list]

    # Assuming all images are 32x32
    image_width, image_height = 64, 64

    # Calculate total rows needed
    total_images = len(images)
    total_rows = (total_images + images_per_row - 1) // images_per_row  # Ceiling division

    # Calculate sprite dimensions
    total_width = images_per_row * image_width + (images_per_row - 1) * padding
    total_height = total_rows * image_height + (total_rows - 1) * padding
    sprite_image = Image.new('RGBA', (total_width, total_height), (255, 255, 255, 0))

    # Prepare a dictionary for JSON output
    sprite_info = {}

    # Place each image on the sprite
    for index, img_path in enumerate(image_list):
        img = images[index]
        x_offset = (index % images_per_row) * (image_width + padding)
        y_offset = (index // images_per_row) * (image_height + padding)
        sprite_image.paste(img, (x_offset, y_offset))

        # Get image name without extension for JSON
        name = os.path.splitext(os.path.basename(img_path))[0]  # Base name without prefix

        # Add image information to the dictionary
        sprite_info[name] = {
            "width": image_width,
            "height": image_height,
            "pixelRatio": 1,  # You can adjust this if needed
            "x": x_offset,
            "y": y_offset
        }

    # Save the sprite image
    sprite_image.save(output_image_path)
    print(f"Sprite image saved at {output_image_path}")

    # Save the JSON output
    with open(json_output_path, 'w') as json_file:
        json.dump(sprite_info, json_file, indent=4)
    print(f"JSON file saved at {json_output_path}")



# Example usage
folder_path = "./vstyles/vnsprite/64"  # Replace with your folder path
output_image_path = "./vstyles/vnsprite/sprite@2x.png"
json_output_path = "./vstyles/vnsprite/sprite@2x.json"
create_sprite_from_folder(folder_path, output_image_path, json_output_path, images_per_row=10, padding=5)
