# ---------------------------------------------------------------------------- #
#                        Black Stripes Detection Script                        #
#                                 André Mattos                                 #
#                             github.com/andrematte                            #
# ---------------------------------------------------------------------------- #

# Objective: Scan all images inside a directory and detect the ones that have 
# black stripes of any thickness. Detected images will be moved into 
# another folder.

# %% 0 - Importing Libraries and Setup
import os, shutil
import cv2
from tqdm import tqdm

formats = ['jpg', 'jped', 'png']
images_path = 'images/'


# %% 1 - Scanning Files
# Scan all files in the image_path directory and returns a list of paths
images = []
for file in os.listdir(images_path):
    if file.split('.')[-1] in formats:
        images.append(os.path.join(images_path, file))

print(f'Detected {len(images)} images inside directory.')
    
    
# %% 2 - Detect images with black stripes of any thickness

# Create folder to move the detected images into
path_to_striped = './images/striped/'
try: os.mkdir(path_to_striped)
except: print('Path already exists')

# Iterate through all the images
for path in tqdm(images):
    image = cv2.imread(path)                                # Read image from path
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # Convert to Grayscale
    blurred = cv2.GaussianBlur(gray, (21,21), 0)            # Apply Gaussian Blur

    # Thresholding to detect black pixels
    T, thresh = cv2.threshold(blurred, 1, 255, cv2.THRESH_BINARY_INV)   # Apply Thresholding

    # Finding Contours
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    true_contours = []                                      # List to store the true contours    
    for contour in contours:
        # Draws a bounding rectangle on contour and check if its width is large enough
        x, y, w, h = cv2.boundingRect(contours[0])
        if w >= image.shape[1]*0.8: 
            true_contours.append(contour)
    
    # If there is at least 1 true contour, draw them and move file into the specified directory
    if len(true_contours) > 0:
        # Drawing Contours to Image
        cv2.drawContours(image, contours, -1, (0,255,0), 4)

        # Saving and moving image
        cv2.imwrite(path, image)
        save_path = path_to_striped + path.replace('images/', '')
        shutil.move(path, save_path)
        
        
        
        