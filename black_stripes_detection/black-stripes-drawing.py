# ---------------------------------------------------------------------------- #
#                         Black Stripes Drawing Script                         #
#                                 André Mattos                                 #
#                             github.com/andrematte                            #
# ---------------------------------------------------------------------------- #

# Objective: This auxiliary script is used to randomly add black stripes to a folder 
# of images. By running this script first, it is possible to create a set of images
# to test the main stripe detection script on.

import random as rd
import os
import cv2

def draw_horizontal_stripe(image):
    '''
    Draws a black horizontal stripe of random thickness and height.
    '''
    height, width, _ = image.shape
    
    color = (0, 0, 0)
    thickness = rd.randint(2, int(height*0.5))
    
    line_height = rd.randint(0, height)
    stripe_start = (0, line_height)
    stripe_end = (width, line_height)

    image = cv2.line(image, stripe_start, stripe_end, color, thickness)
    
    return image

rd.seed(23)
formats = ['jpg', 'jped', 'png']
images_path = 'images/'

# %% 1 - Scanning Files
images = []
for file in os.listdir(images_path):
    if file.split('.')[-1] in formats:
        images.append(os.path.join(images_path, file))

print(f'Detected {len(images)} images inside directory.')


# %% 2 - Select random images to add stripes
number_of_selected_images = len(images)*0.1
selected_images = rd.sample(images, int(number_of_selected_images))
print(f'Adding stripes to {len(selected_images)} images.')

# %% 3 - Add stripes to selected images
for path in selected_images:
    image = cv2.imread(path)
    striped = draw_horizontal_stripe(image)
    cv2.imwrite(path, striped)
    
        
        


