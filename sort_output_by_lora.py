import os
import re
from PIL import Image

# Find all the PNG files in the current directory
png_files = [f for f in os.listdir() if f.endswith('.png')]

# Ask the user which <lora> they want to use
choice = int(input("Enter the position in the promopts of the <lora> you want to use starting with 1(if not found -1): "))

# Loop over each PNG file
for png_file in png_files:
    # Open the image and extract its metadata
    with Image.open(png_file) as img:
        metadata = img.info

    # Find all the <lora> strings and store them in a list
    loras = re.findall(r'<lora:([^>]+)>', metadata['parameters'])

    i = choice-1

    if len(loras) > 0:
        if i < 0 or i >= len(loras):
            i = len(loras) - 1

        chosen_lora = loras[i].split(":")[0]
    else:
        chosen_lora = "no_lora"

    # Create a new folder with the chosen lora name
    os.makedirs(chosen_lora, exist_ok=True)

    # Move the file to the new folder
    old_filename = png_file
    new_filename = os.path.join(chosen_lora, old_filename)
    os.rename(old_filename, new_filename)
    print(f"{old_filename} moved to {chosen_lora}")