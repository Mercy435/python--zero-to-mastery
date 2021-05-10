# save to new folder

import sys
import os
from PIL import Image


# grab first and second argument # use the sys.argv to assign the folders
image_folder = sys.argv[1]
output_folder = sys.argv[2]  # run in terminal

print(image_folder, output_folder)

# check is new/exists, if not create, using the os or pathlib module
print(os.path.exists(output_folder))  # this returns false when run in a terminal
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # use this to make a new directory with name assigned to the output folder
# line 15 now returns true
#
#
# loop through folder with jpg images
for filename in os.listdir(image_folder):  # listdir lists items in dir
    img = Image.open(f'{image_folder}{filename}')  # open the images in the right path
    # img = Image.open(r'/imagejpg/')
    clean_name = os.path.splitext(filename) # this gives the name and the extension in a tuple, do an index to assess
#     only the name
    print(clean_name)
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
