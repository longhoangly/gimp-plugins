#! /usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import check_output

cmd = '(python-fu-watermark RUN-INTERACTIVE "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_08/IMG_1688_copy.JPG" "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_08/Watermark-4.png")'

output = check_output(['/Applications/GIMP-2.10.app/Contents/MacOS/gimp',
                       # '-i', '-b', cmd, '-b', '(gimp-quit 0)'])
                       '-b', cmd, '-b', '(gimp-quit 0)'])

print(output)
