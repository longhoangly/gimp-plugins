#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from base import *
from subprocess import *
from sys import platform

[images_dir, image_pattern, watermark_path, watermark_text, watermark_font_name,
    watermark_font_size, debug, debug_image, has_gui, gimp_path] = get_opts(sys.argv[1:])

# Finding images
images = [f for f in os.listdir(images_dir) if re.match(image_pattern, f)]
print('')
print(images)

if not debug:
    proceeded_index = 1

    for image in images:

        new_file_name = os.path.join(images_dir, 'ImgLogo_' + image)
        if '' != watermark_text:
            new_file_name = os.path.join(images_dir, 'TxTLogo_' + image)

        image_path = os.path.join(images_dir, image)

        image_path = image_path.replace("\\", "/")
        new_file_name = new_file_name.replace("\\", "/")
        print('Running PROCESS mode, checking image: {}\n'.format(new_file_name))

        if not os.path.exists(new_file_name) and "ImgLogo_" not in image and "TxtLogo_" not in image:
            print('Percentage: {}/{}, {:.2%}%'.format(proceeded_index,
                                                      len(images), float(proceeded_index)/float(len(images))))
            print('Processing image {}: {}\n'.format(
                proceeded_index, image_path))

            if '' != watermark_text:
                add_text_watermark(
                    image_path, watermark_text, watermark_font_name, watermark_font_size, has_gui, gimp_path)
            else:
                add_image_watermark(image_path, watermark_path, has_gui, gimp_path)

        else:
            print('Skip the image {}: already add logo watermark!\n'.format(image_path))

        proceeded_index += 1
else:

    image_path = os.path.join(images_dir, debug_image)
    print('Running DEBUG mode, processing image: {}\n'.format(image_path))

    if '' != watermark_text:
        add_text_watermark(
            image_path, watermark_text, watermark_font_name, watermark_font_size, has_gui, gimp_path)
    else:
        add_image_watermark(image_path, watermark_path, has_gui, gimp_path)


print('------------------------------------------------------------------------------------------')
print('Well done. Finished all works! Please check result at: {}'.format(images_dir))
print('------------------------------------------------------------------------------------------\n')

if debug:
    head, tail = os.path.split(image_path)
    new_file_name = os.path.join(head, 'ImgLogo_' + tail)
    if '' != watermark_text:
            new_file_name = os.path.join(head, 'TxtLogo_' + tail)

    if "win" in platform:
        new_file_name = new_file_name.replace("/", "\\")
        try:
            check_output("explorer {}".format(new_file_name))
        except:
            print("Exception...")
    else:
        check_output(["open", new_file_name])
else:
    if "win" in platform:
        images_dir = images_dir.replace("/", "\\")
        try:
            check_output("explorer \"{}\"".format(images_dir))
        except:
            print("Exception...")
    else:
        check_output(["open", images_dir])
