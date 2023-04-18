from PIL import Image
import glob
import json
import shutil
import os

# Config
dataset = 'basel'
# images = glob.glob(f"{dataset}/*.jpg")
with open(f'{dataset}/output_json.json', "r") as file:
    selected_images = json.load(file)
# os.mkdir(f"output_selected/{dataset}")
# Filter selected panoramas
for image in selected_images:
    objects = image['objects']
    for d in objects:
        if 'Bomb' in d:
            if d['Bomb']['score'] > 0.7:
                shutil.copyfile(f"{dataset}/{image['id']}.jpg",
                                f"output_selected/{dataset}/{image['id']}.jpg")  # {str(d['Bomb']['score'])[:4]}

# Translate coordinates for crop


def translate_coordinate(coord, cropped_coord, cropped_size, original_size):
    """
    Translates a coordinate from a cropped image to the original image.

    Args:
        coord (tuple): x and y coordinates of the point to translate.
        cropped_coord (tuple): x and y coordinates of the top-left corner of the cropped image.
        cropped_size (tuple): width and height of the cropped image.
        original_size (tuple): width and height of the original image.

    Returns:
        tuple: x and y coordinates of the translated point on the original image.
    """
    # calculate the coordinates of the cropped image relative to the original image
    cropped_left, cropped_top = cropped_coord
    original_left = cropped_left + left_side_left
    original_top = cropped_top + left_side_top

    # calculate the ratio of the original image size to the cropped image size
    ratio_x = original_size[0] / cropped_size[0]
    ratio_y = original_size[1] / cropped_size[1]

    # scale the coordinates back up to the original image size
    translated_coord = (
        int(original_left + coord[0] * ratio_x),
        int(original_top + coord[1] * ratio_y)
    )

    return translated_coord


# left_left = int(16384 * 0.5 * 0.12)
# left_top = int(8192 * 0.5 * 0.35)
# translate_coordinate(coord, cropped_coord, cropped_size, original_size)
# translate_coordinate(coord, cropped_coord, cropped_size, original_size)

# # Open the image
# cropimage = Image.open("_m5BUSNfAhBNG_0bi24wcw.jpg")

# # Get the size of the image
# width, height = image.size
# # 16384 × 8192
# # [0.4164752  0.6158229  0.6953179  0.74813735]

# # Define the crop boundaries
# left = int(width * 0.6158229)
# top = int(height * 0.4164752)
# right = int(width * 0.74813735)
# bottom = int(height * 0.6953179)

# # Crop the image
# cropped_image = image.crop((left, top, right, bottom))

# # Save the cropped image
# cropped_image.save("_m5BUSNfAhBNG_0bi24wcw_crop.jpg")
