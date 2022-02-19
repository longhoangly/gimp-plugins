#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
from subprocess import check_output


def add_image_watermark(image_path, watermark_path, has_gui):

    run_mode = "RUN-INTERACTIVE" if has_gui else "RUN-NONINTERACTIVE"
    command = '(python-fu-image-watermark {} "{}" "{}" {})'.format(run_mode,
                                                                   image_path, watermark_path, has_gui)
    execute_gimp_command(command, has_gui)


def add_text_watermark(image_path, watermark_text, watermark_font_name, watermark_font_size, has_gui):

    run_mode = "RUN-INTERACTIVE" if has_gui else "RUN-NONINTERACTIVE"
    command = '(python-fu-text-watermark {} "{}" "{}" "{}" {} {})'.format(run_mode,  image_path,
                                                                          watermark_text, watermark_font_name, watermark_font_size, has_gui)
    execute_gimp_command(command, has_gui)


def execute_gimp_command(command, has_gui):

    if(has_gui):
        output = check_output(
            ['/Applications/GIMP-2.10.app/Contents/MacOS/gimp', '-b', command, '-b', '(gimp-quit 0)'])
    else:
        output = check_output(
            ['/Applications/GIMP-2.10.app/Contents/MacOS/gimp', '-i', '-b', command, '-b', '(gimp-quit 0)'])

    print("\n-----------------")
    print("GIMP output...")
    print(output.decode())


def get_opts(argv):

    try:
        opts, args = getopt.getopt(
            argv, "h:", ["help", "images_dir=", "image_pattern=", "watermark_path=", "watermark_text=", "font_name=", "font_size=", "debug=", "debug_image=", "has_gui="])

    except getopt.GetoptError as err:
        print(err)
        usage()

    images_dir = ''
    image_pattern = r'IMG_.[0-9]+.JPG$'
    watermark_path = ''
    watermark_text = ''
    watermark_font_name = ''
    watermark_font_size = ''
    debug = 0
    debug_image = ''
    has_gui = 0

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt == "--images_dir":
            images_dir = arg
        elif opt == "--image_pattern":
            image_pattern = arg
        elif opt == "--watermark_path":
            watermark_path = arg
        elif opt == "--watermark_text":
            watermark_text = arg
        elif opt == "--font_name":
            watermark_font_name = arg
        elif opt == "--font_size":
            watermark_font_size = arg
        elif opt == "--debug":
            debug = arg
        elif opt == "--debug_image":
            debug_image = arg
        elif opt == "--has_gui":
            has_gui = arg

    print([images_dir, image_pattern, watermark_path, watermark_text,
          watermark_font_name, watermark_font_size, debug, debug_image, has_gui])

    if ('' == images_dir) or (debug == '1' and '' == debug_image):
        print('Missing images_dir or debug_image (in case debug = 1)')
        usage()

    if '' != watermark_font_size:
        watermark_font_size = int(watermark_font_size)

    if '' != debug:
        debug = int(debug)

    if '' != has_gui:
        has_gui = int(has_gui)

    print([images_dir, image_pattern, watermark_path, watermark_text,
          watermark_font_name, watermark_font_size, debug, debug_image, has_gui])

    return [images_dir, image_pattern, watermark_path, watermark_text, watermark_font_name, watermark_font_size, debug, debug_image, has_gui]


def usage():

    print('\nSomething is wrong?! Please refer to below command format to correct it.')

    # sys.argv[0] contains script name!
    print('Usage: {} --images_dir <images_dir> --image_pattern <image_pattern> --watermark_path <watermark_path> \n \
                    --watermark_text <watermark_text> --watermark_font_name <watermark_font_name> --watermark_font_size <watermark_font_size> \n \
                    --debug <debug> --debug_image <debug_image> --has_gui <has_gui>\n'.format(sys.argv[0]))

    sys.exit(0)
