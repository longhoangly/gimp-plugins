#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import gimp
import gimpcolor
from gimpfu import *


def text_watermark(image, text, fontname, fontsize, has_gui):

    # load main image
    image_obj = pdb.gimp_file_load(image, image)

    # add text watermark (0 = GIMP_UNIT_PIXEL, 3 = GIMP_UNIT_POINT)
    watermark_layer = pdb.gimp_text_layer_new(
        image_obj, text, fontname, fontsize, 3)
    pdb.gimp_image_add_layer(image_obj, watermark_layer, 0)

    pdb.gimp_layer_set_opacity(watermark_layer, 80)
    pdb.gimp_layer_set_offsets(
        watermark_layer, 200, image_obj.height - watermark_layer.height + 200)

    # create background layer (opacity 50)
    bg_water_layer = pdb.gimp_layer_new(image_obj, watermark_layer.width,
                                        200,
                                        0, "bg_water_layer",
                                        50, 0)
    pdb.gimp_image_add_layer(image_obj, bg_water_layer, 1)

    pdb.gimp_layer_set_offsets(
        bg_water_layer, 200, image_obj.height - watermark_layer.height * 3 / 4 + 300)

    # set background color (opacity 40)
    foreground = gimpcolor.RGB(112, 128, 144)
    pdb.gimp_context_set_foreground(foreground)
    pdb.gimp_bucket_fill(bg_water_layer, 0, 0, 40, 100, 0, 0, 0)

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
    'python-fu-text-watermark',
    'Adding text watermark for an image',
    'A simple script adds text watermark.',
    'Long Ly',
    '(c) GPL V3.0 or later',
    'Feb 2022',
    '<Toolbox>/Functionality/Text Watermark',
    '',
    [
        (PF_FILE, 'file', 'Image', None),
        (PF_STRING, 'text', 'Watermark Text', ''),
        (PF_STRING, 'fontname', 'Text Font Name', 'Sans'),
        (PF_INT32, 'fontsize', 'Text Font Size', 25),
        (PF_TOGGLE, 'has_gui', 'Running with GUI?', True)
    ],
    [],
    text_watermark)

main()
