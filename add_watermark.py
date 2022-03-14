#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from base import *
from subprocess import *

[images_dir, image_pattern, watermark_path, watermark_text, watermark_font_name,
    watermark_font_size, debug, debug_image, has_gui] = get_opts(sys.argv[1:])

# Finding images
images = [f for f in os.listdir(images_dir) if re.match(image_pattern, f)]
print('')
print(images)

if not debug:
    proceeded_index = 1

    for image in images:

        new_file_name = os.path.join(images_dir, 'Marked_' + image)
        image_path = os.path.join(images_dir, image)
        print('Running PROCESS mode, checking image: {}\n'.format(new_file_name))

        if not os.path.exists(new_file_name):
            print('Percentage: {}/{}, {:.2%}%'.format(proceeded_index,
                                                      len(images), float(proceeded_index)/float(len(images))))
            print('Processing image {}: {}\n'.format(
                proceeded_index, image_path))

            if '' != watermark_text:
                add_text_watermark(
                    image_path, watermark_text, watermark_font_name, watermark_font_size, has_gui)
            else:
                add_image_watermark(image_path, watermark_path, has_gui)

        else:
            print('Skip the image {}: already marked!\n'.format(image_path))

        proceeded_index += 1
else:

    image_path = os.path.join(images_dir, debug_image)
    print('Running DEBUG mode, processing image: {}\n'.format(image_path))

    if '' != watermark_text:
        add_text_watermark(
            image_path, watermark_text, watermark_font_name, watermark_font_size, has_gui)
    else:
        add_image_watermark(image_path, watermark_path, has_gui)


print('------------------------------------------------------------------------------------------')
print('Well done. Finished all works! Please check result at: {}'.format(images_dir))
print('------------------------------------------------------------------------------------------\n')

if debug:
    head, tail = os.path.split(image_path)
    new_file_name = os.path.join(head, 'Marked_' + tail)
    check_output(['open', new_file_name])
else:
    check_output(['open', images_dir])
