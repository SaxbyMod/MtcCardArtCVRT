import os
from PIL import Image

# Directory containing the original images
old_sprites_dir = "old"

# Destination directory for new images
new_sprites_dir = "new"

# Create the destination directory if it doesn't exist
if not os.path.exists(new_sprites_dir):
    os.makedirs(new_sprites_dir)

# Iterate over the original images
for filename in os.listdir(old_sprites_dir):
    print(filename)
    # Path to the original image
    old_image_path = os.path.join(old_sprites_dir, filename)

    # Open the original image and convert it to RGBA mode
    img = Image.open(old_image_path).convert("RGBA")

    # Get the dimensions of the original image
    width, height = img.size

    # Determine the larger dimension
    max_dim = max(width, height)

    # Calculate the paste coordinates to center the old image in the new image
    paste_x = (max_dim - width) // 2
    paste_y = (max_dim - height) // 2

    # Create a new image with the larger dimension
    new_img = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))

    # Paste the old image onto the new image
    new_img.paste(img, (paste_x, paste_y))

    # Generate the new filename
    new_filename = f"{filename}"
    print(filename + "Completed")
    # Save the new image
    new_image_path = os.path.join(new_sprites_dir, new_filename)
    new_img.save(new_image_path)

    # Close the images
    img.close()
    new_img.close()