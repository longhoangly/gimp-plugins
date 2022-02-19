#!/usr/bin/python
# -*- coding: utf-8 -*-

import gimpcolor
from gimpfu import pdb


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
