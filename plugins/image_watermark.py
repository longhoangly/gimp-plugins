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

    # load watermark as a layer (opacity 60)
    watermark_layer = pdb.gimp_file_load_layer(image_obj, watermark)
    pdb.gimp_image_add_layer(image_obj, watermark_layer, 0)
    pdb.gimp_layer_set_opacity(watermark_layer, 60)

    # scale watermark
    scale_rate = image_obj.height / (watermark_layer.height * 7)
    print('scale rate {}'.format(scale_rate))

    new_width = watermark_layer.width * scale_rate
    new_height = watermark_layer.height * scale_rate
    print('new_width {}'.format(new_width))
    print('new_height {}'.format(new_height))

    pdb.gimp_layer_scale(watermark_layer, new_width, new_height, 0)

    # add background layer (opacity 30)
    bg_water_layer = pdb.gimp_layer_new(image_obj, watermark_layer.width,
                                        watermark_layer.height,
                                        0, "bg_water_layer",
                                        30, 0)
    pdb.gimp_image_add_layer(image_obj, bg_water_layer, 1)

    # watermark and background offsets
    width_offset = image_obj.width / 30
    height_offset = image_obj.height - watermark_layer.height - width_offset
    pdb.gimp_layer_set_offsets(watermark_layer, width_offset, height_offset)
    pdb.gimp_layer_set_offsets(bg_water_layer, width_offset, height_offset)

    # set background color (opacity 50)
    foreground = gimpcolor.RGB(0, 0, 0)
    pdb.gimp_context_set_foreground(foreground)
    pdb.gimp_bucket_fill(bg_water_layer, 0, 0, 50, 200, 0, 0, 0)

    # display the image (GUI mode)
    if has_gui:
        pdb.gimp_display_new(image_obj)
        pdb.gimp_displays_flush()

    # merge all layers into one
    merged_layer = pdb.gimp_image_merge_visible_layers(
        image_obj, CLIP_TO_IMAGE)

    # save as new file
    head, tail = os.path.split(image)
    new_file_name = os.path.join(head, 'ImgLogo_' + tail)
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
