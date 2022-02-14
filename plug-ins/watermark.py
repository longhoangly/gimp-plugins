#!/Applications/GIMP-2.10.app/Contents/MacOS/python

from gimpfu import *


def watermark(file, water):
    # load image
    image = pdb.gimp_file_load(file, file)

    # add watermark image as a layer
    layer = pdb.gimp_file_load_layer(image, water)
    image.add_layer(layer, 0)

    # display the image
    pdb.gimp_display_new(image)
    pdb.gimp_displays_flush()

    # merge all layers
    merged_layer = pdb.gimp_image_merge_visible_layers(image, CLIP_TO_IMAGE)

    
    pdb.gimp_file_save(image, merged_layer, '/temp/tq84_write_text.png', '?')
    pdb.gimp_image_delete(image)


register(
    'python-fu-watermark',
    'Adding watermark for an image',
    'A simple script adds watermark.',
    'Long Ly',
    '(c) GPL V3.0 or later',
    'Feb 2022',
    '<Toolbox>/Functionality/Watermark',
    '',
    [
        (PF_FILE, 'file', 'Image', None),
        (PF_FILE, 'water', 'Watermark', None)
    ],
    [],
    watermark)

main()
