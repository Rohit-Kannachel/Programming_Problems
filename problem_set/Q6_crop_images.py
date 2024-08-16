# There are about 100 images on a remote server
# they are of an unsuitable size for a ML model, they need to be cropped to 400 x 400

# SSH into the server and copy the folder of images onto your local computer

# Load the images using an image library e.g. PIL

# using numpy/PIL/any resource, crop the images into the required size

# save these cropped images into a new folder called "Cropped Images"

# use SSH to copy the new folder back into the server

## Make 2 folders:
# One will be cropped to the corner(defult)
# One will be cropped to the center(cosmetic)

### Write the python code to read, copy and write files here ###
#C:\Users\mvela\OneDrive\Documents\Code\test

from PIL import Image as img
import os
import numpy as np
from tqdm import tqdm

image_path = r"C:\Users\mvela\OneDrive\Documents\Code\test"
list_of_images = os.listdir(image_path)

def crop_folder():
    """
    If the function detects that the 'test_cropped' folder doesn't exist, it makes one.
    """
    if not os.path.exists(r"C:\Users\mvela\OneDrive\Documents\Code\test_cropped"):
        os.mkdir(r"C:\Users\mvela\OneDrive\Documents\Code\test_cropped")
    return None

def image_cycle():
    crop_folder()
    count = 0
    for photo in tqdm(list_of_images):
        image_processing = img.open(rf"{image_path}\{photo}")
        
        # Get dimensions of the image
        width, height = image_processing.size
        
        # Calculate cropping coordinates to crop from the center
        start_col = (width - 400) // 2
        end_col = start_col + 400
        start_row = (height - 400) // 2
        end_row = start_row + 400
        
        cropped_array = np.array(image_processing)[start_row:end_row, start_col:end_col]
        result = img.fromarray(cropped_array)
        result.save(rf"C:\Users\mvela\OneDrive\Documents\Code\test_cropped\cropped_photo{count}.png")
        count += 1

image_cycle()

"""
An Example of Cropping
"""
# start_row = 0
# end_row = 183

# start_col = 0
# end_col = 275


# dog = img.open(r"C:\Users\mvela\OneDrive\Documents\Code\Scratch\Week1\dog_image.jpg")
# dog_array= np.array(dog)
# cropped_image = dog_array[start_row:end_row, start_col:end_col, :] #last row is rgb range

# plt.imshow(cropped_image)
# plt.show()
