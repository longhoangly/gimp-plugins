#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
from subprocess import check_output


def add_image_watermark(image_path, watermark_path, has_gui, gimp_path):

    run_mode = "RUN-INTERACTIVE" if has_gui else "RUN-NONINTERACTIVE"
    command = '(python-fu-image-watermark {} "{}" "{}" {})'.format(run_mode,
                                                                   image_path, watermark_path, has_gui)
    execute_gimp_command(command, has_gui, gimp_path)


def add_text_watermark(image_path, watermark_text, watermark_font_name, watermark_font_size, has_gui, gimp_path):

    run_mode = "RUN-INTERACTIVE" if has_gui else "RUN-NONINTERACTIVE"
    command = '(python-fu-text-watermark {} "{}" "{}" "{}" {} {})'.format(run_mode,  image_path,
                                                                          watermark_text, watermark_font_name, watermark_font_size, has_gui)
    execute_gimp_command(command, has_gui, gimp_path)


def execute_gimp_command(command, has_gui, gimp_path):

    if(has_gui):
        output = check_output(
            [gimp_path, '-b', command, '-b', '(gimp-quit 0)'])
    else:
        output = check_output(
            [gimp_path, '-i', '-b', command, '-b', '(gimp-quit 0)'])

    print("\n-----------------")
    print("GIMP output...")
    print(output.decode())


def get_opts(argv):

    try:
        opts, args = getopt.getopt(
            argv, "h:", ["help", "images_dir=", "image_pattern=", "watermark_path=", "watermark_text=", "font_name=", "font_size=", "debug=", "debug_image=", "has_gui=", "gimp_path="])

    except getopt.GetoptError as err:
        print(err)
        usage()

    images_dir = ''
    image_pattern = r'.*\..*'
    watermark_path = ''
    watermark_text = ''
    watermark_font_name = ''
    watermark_font_size = ''
    debug = 0
    debug_image = ''
    has_gui = 0
    gimp_path = ''

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
        elif opt == "--gimp_path":
            gimp_path = arg

    print([images_dir, image_pattern, watermark_path, watermark_text,
          watermark_font_name, watermark_font_size, debug, debug_image, has_gui, gimp_path])

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
          watermark_font_name, watermark_font_size, debug, debug_image, has_gui, gimp_path])

    return [images_dir, image_pattern, watermark_path, watermark_text, watermark_font_name, watermark_font_size, debug, debug_image, has_gui, gimp_path]


def usage():

    print('\nSomething is wrong?! Please refer to below command format to correct it.')

    # sys.argv[0] contains script name!
    print('Usage: {} --images_dir <images_dir> --image_pattern <image_pattern> --watermark_path <watermark_path> \n \
                    --watermark_text <watermark_text> --watermark_font_name <watermark_font_name> --watermark_font_size <watermark_font_size> \n \
                    --debug <debug> --debug_image <debug_image> --has_gui <has_gui> --gimp_path <gimp_path>\n'.format(sys.argv[0]))

    sys.exit(0)
