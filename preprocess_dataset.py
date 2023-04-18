from PIL import Image
import glob
import os

# Config
dataset = 'basel'
images = glob.glob(f"{dataset}/*.jpg")


def crop_image(path, crop_left, crop_right, crop_top, crop_bottom):
    # open the image
    image = Image.open(path)

    # get the new size of the image
    width, height = image.size
    new_size = (int(width/3), int(height/3))

    # resize the image
    resized_image = image.resize(new_size)

    # calculate the coordinates to crop the left side of the image
    left = 0
    top = 0
    right = int(new_size[0]/2)
    bottom = new_size[1]

    # crop the left side of the image
    left_side = resized_image.crop((left, top, right, bottom))

    # calculate the coordinates to crop the right side of the image
    left = int(new_size[0]/2)
    top = 0
    right = new_size[0]
    bottom = new_size[1]

    # crop the right side of the image
    right_side = resized_image.crop((left, top, right, bottom))

    # get the original size of the images
    left_width, left_height = left_side.size
    right_width, right_height = right_side.size

    # calculate the coordinates to crop the left side image
    left_left = int(left_width * crop_left)
    left_top = int(left_height * crop_top)
    left_right = int(left_width * (1 - crop_right))
    left_bottom = int(left_height * (1 - crop_bottom))

    # calculate the coordinates to crop the right side image
    right_left = int(right_width * crop_left)
    right_top = int(right_height * crop_top)
    right_right = int(right_width * (1 - crop_right))
    right_bottom = int(right_height * (1 - crop_bottom))

    # crop the left side image
    left_side_cropped = left_side.crop(
        (left_left, left_top, left_right, left_bottom))

    # crop the right side image
    right_side_cropped = right_side.crop(
        (right_left, right_top, right_right, right_bottom))

    # save both sides of the cropped images
    if not os.path.exists(f'{dataset}_preprocess'):
        os.mkdir(f'{dataset}_preprocess')
    left_side_cropped.save(
        f"{dataset}_preprocess/{path.replace(f'{dataset}/', '')[:-4]}_l.jpg")
    right_side_cropped.save(
        f"{dataset}_preprocess/{path.replace(f'{dataset}/', '')[:-4]}_r.jpg")


for image in images:
    os.system('clear')
    print(f'{images.index(image)+1}/{len(images)+1}')
    crop_image(image, 0.12, 0.12, 0.35, 0.35)
