#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import gimp
import gimpcolor
from gimpfu import pdb
from gimpfu import pdb, register, PF_FILE, PF_TOGGLE, PF_STRING, PF_INT32, CLIP_TO_IMAGE, main


def add_text_watermark(image_obj, text, fontname, fontsize, has_background):

    # add text watermark (0 = GIMP_UNIT_PIXEL, 3 = GIMP_UNIT_POINT)
    watermark_layer = pdb.gimp_text_layer_new(
        image_obj, text, fontname, fontsize, 3)
    pdb.gimp_image_add_layer(image_obj, watermark_layer, 0)
    pdb.gimp_layer_set_opacity(watermark_layer, 70)

    # watermark text color and offsets
    text_color = gimpcolor.RGB(255, 255, 255)
    pdb.gimp_text_layer_set_color(watermark_layer, text_color)
    pdb.gimp_layer_set_offsets(watermark_layer, 0, 0)

    bg_water_layer = None
    if has_background:
        # add background layer (opacity 50)
        bg_water_layer = pdb.gimp_layer_new(image_obj, watermark_layer.width + watermark_layer.width * 2/30,
                                            watermark_layer.height,
                                            0, "bg_water_layer",
                                            50, 0)
        pdb.gimp_image_add_layer(image_obj, bg_water_layer, 1)
        pdb.gimp_layer_set_offsets(bg_water_layer, 0, 0)

        # set background color (opacity 100)
        foreground = gimpcolor.RGB(0, 0, 0)
        pdb.gimp_context_set_foreground(foreground)
        pdb.gimp_bucket_fill(bg_water_layer, 0, 0, 100, 200, 0, 0, 0)

    return [watermark_layer, bg_water_layer]


def set_watermark_offsets(watermark_layer, bg_water_layer, width_offset, height_offset, has_background):

    pdb.gimp_layer_set_offsets(watermark_layer, width_offset, height_offset)

    if has_background:
        pdb.gimp_layer_set_offsets(
            bg_water_layer, width_offset - watermark_layer.width / 30, height_offset)


# Main method
def text_watermark(image, text, fontname, fontsize, has_gui):

    # load main image
    image_obj = pdb.gimp_file_load(image, image)

    # add first text watermark (lower & left)
    [watermark_layer, bg_water_layer] = add_text_watermark(
        image_obj, text, fontname, fontsize, 0)

    width_offset = image_obj.width / 30
    height_offset = image_obj.height - watermark_layer.height - image_obj.width / 30
    set_watermark_offsets(watermark_layer, bg_water_layer, width_offset,
                          height_offset, 0)

    # add second text watermark (central)
    # [watermark_layer, bg_water_layer] = add_text_watermark(
    #     image_obj, text, fontname, fontsize, 0)

    # width_offset = image_obj.width * 12 / 30
    # height_offset = image_obj.height / 2 - image_obj.width / 30
    # set_watermark_offsets(watermark_layer, bg_water_layer, width_offset,
    #                       height_offset, 0)

    # add third text watermark (upper & right)
    [watermark_layer, bg_water_layer] = add_text_watermark(
        image_obj, text, fontname, fontsize, 0)

    width_offset = image_obj.width - watermark_layer.width - image_obj.width / 30
    height_offset = image_obj.width / 30
    set_watermark_offsets(watermark_layer, bg_water_layer, width_offset,
                          height_offset, 0)

    # display the image (GUI mode)
    if has_gui:
        pdb.gimp_display_new(image_obj)
        pdb.gimp_displays_flush()

    # merge all layers into one
    merged_layer = pdb.gimp_image_merge_visible_layers(
        image_obj, CLIP_TO_IMAGE)

    # save as new file
    head, tail = os.path.split(image)
    new_file_name = os.path.join(head, 'TxtLogo_' + tail)
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