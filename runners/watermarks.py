#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from subprocess import check_output


# Set GUI config (0 - no GUI, 1 - has GUI)
has_gui = 0

# Set input image and watermark
image_pattern = r"IMG_.[0-9]+.JPG$"
images_path = "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_15"
watermark_path = "/Users/long.lyhoang/Downloads/Bep Co Vy/Watermark-4.png"

images = [f for f in os.listdir(images_path) if re.match(image_pattern, f)]
print(images)


# Main method
def add_watermark(image_path, watermark_path):

    run_mode = "RUN-INTERACTIVE" if has_gui else "RUN-NONINTERACTIVE"
    cmd = '(python-fu-watermark {} "{}" "{}" {})'.format(run_mode,
                                                         image_path, watermark_path, has_gui)
    if(has_gui):
        output = check_output(
            ['/Applications/GIMP-2.10.app/Contents/MacOS/gimp', '-b', cmd, '-b', '(gimp-quit 0)'])
    else:
        output = check_output(
            ['/Applications/GIMP-2.10.app/Contents/MacOS/gimp', '-i', '-b', cmd, '-b', '(gimp-quit 0)'])

    print("Process call output...")
    print(output)


# Calling point to process images
proceeded_index = 1
for image in images:

    new_file_name = os.path.join(images_path, 'Marked_' + image)
    print('checking image: {}'.format(new_file_name))

    image_path = os.path.join(images_path, image)
    if not os.path.exists(new_file_name):
        print('percentage: {}/{}, {:.2%}%'.format(proceeded_index,
              len(images), float(proceeded_index)/float(len(images))))
        print('processing image {}: {}'.format(proceeded_index, image_path))
        add_watermark(image_path, watermark_path)
    else:
        print('Skip the image {}: already marked!'.format(image_path))

    proceeded_index += 1


# Debug
# debug_image = "Marked_IMG_1677.JPG"
# image_path = os.path.join(images_path, debug_image)
# print('processing debug image: {}'.format(image_path))
# add_watermark(image_path, watermark_path)
