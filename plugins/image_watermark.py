#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import os
import gimp
import gimpcolor
from gimpfu import pdb, register, PF_FILE, PF_TOGGLE, CLIP_TO_IMAGE, main


def image_watermark(image, watermark, has_gui):

    # load main image
    image_obj = pdb.gimp_file_load(image, image)

    # load watermark as a layer
    watermark_layer = pdb.gimp_file_load_layer(image_obj, watermark)
    pdb.gimp_image_add_layer(image_obj, watermark_layer, 0)

    # scale watermark based on main image obj
    rate = image_obj.height / (watermark_layer.height * 4)
    print('scale rate {}'.format(rate))

    new_width = watermark_layer.width * rate
    new_height = watermark_layer.height * rate
    print('new_width {}'.format(new_width))
    print('new_height {}'.format(new_height))

    pdb.gimp_layer_scale(
        watermark_layer, new_width, new_height, 0)

    # edit watermark opacity and offsets
    pdb.gimp_layer_set_opacity(watermark_layer, 80)
    pdb.gimp_layer_set_offsets(
        watermark_layer, watermark_layer.width / 4, image_obj.height * 4 / 5)

    # create background layer (opacity 50)
    bg_water_layer = pdb.gimp_layer_new(image_obj, watermark_layer.width,
                                        watermark_layer.height * 2 / 5,
                                        0, "bg_water_layer",
                                        50, 0)
    pdb.gimp_image_add_layer(image_obj, bg_water_layer, 1)

    pdb.gimp_layer_set_offsets(
        bg_water_layer, watermark_layer.width / 4, image_obj.height * 7 / 8)

    # set background color (opacity 100)
    foreground = gimpcolor.RGB(0, 0, 0)
    pdb.gimp_context_set_foreground(foreground)
    pdb.gimp_bucket_fill(bg_water_layer, 0, 0, 100, 200, 0, 0, 0)

    # display the image (GUI mode)
    if has_gui:
        pdb.gimp_display_new(image_obj)
        pdb.gimp_displays_flush()

    # merge all layers into one
    merged_layer = pdb.gimp_image_merge_visible_layers(
        image_obj, CLIP_TO_IMAGE)

    # save as new file
    head, tail = os.path.split(image)
    new_file_name = os.path.join(head, 'Marked_' + tail)
    print('Output file: {}'.format(new_file_name))
    pdb.gimp_file_save(image_obj, merged_layer, new_file_name, '?')

    # delete display and image (GUI mode)
    if has_gui:
        for displayID in range(1, image_obj.ID+50):
            display = gimp._id2display(displayID)
            if isinstance(display, gimp.Display):
                print('Image: %d; Display: %d' % (image_obj.ID, displayID))
                break
        if not display:
            raise Exception('Display not found')
        gimp.delete(display)


register(
    'python-fu-image-watermark',
    'Adding image watermark for another image',
    'A simple script adds image watermark.',
    'Long Ly',
    '(c) GPL V3.0 or later',
    'Feb 2022',
    '<Toolbox>/Functionality/Image Watermark',
    '',
    [
        (PF_FILE, 'file', 'Image', None),
        (PF_FILE, 'watermark', 'Watermark', None),
        (PF_TOGGLE, 'has_gui', 'Running with GUI?', True)
    ],
    [],
    image_watermark)

main()
