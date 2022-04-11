#!/bin/zsh

echo
echo Starting add watermark process...

xxx="long.lyhoang"

# [Image Watermark + No Debug]
python3 -B add_watermark.py --images_dir "/Users/${xxx}/Downloads/canon/new" \
    --watermark_path "/Users/${xxx}/Downloads/canon/Watermark-5.png" \
    --has_gui 0 \
    --gimp_path "/Applications/GIMP-2.10.app/Contents/MacOS/gimp"

# [Image Watermark + Debug]
# python3 -B add_watermark.py --images_dir "/Users/${xxx}/Downloads/canon/2022_02_16" \
#     --watermark_path "/Users/${xxx}/Downloads/canon/Watermark-5.png" \
#     --debug_image "IMG_1755.JPG" \
#     --debug 1 \
#     --has_gui 0 \
#     --gimp_path "/Applications/GIMP-2.10.app/Contents/MacOS/gimp"

# python3 -B add_watermark.py --images_dir "/Users/${xxx}/Downloads/canon" \
#     --watermark_path "/Users/${xxx}/Downloads/canon/BepCoVy-1.png" \
#     --debug_image "3d83a3ef7d22b17ce833.jpg" \
#     --debug 1 \
#     --has_gui 0 \
#     --gimp_path "/Applications/GIMP-2.10.app/Contents/MacOS/gimp"

# [Text Watermark + No Debug]
# python3 -B add_watermark.py --images_dir "/Users/${xxx}/Downloads/canon/2022_02_16" \
#     --watermark_text "Bếp Cô Vy" \
#     --font_name "FleurDeLeah" \
#     --font_size 30 \
#     --has_gui 0 \
#     --gimp_path "/Applications/GIMP-2.10.app/Contents/MacOS/gimp"

# [Text Watermark + Debug]
# python3 -B add_watermark.py --images_dir "/Users/${xxx}/Downloads/canon/2022_02_16" \
#     --debug_image "IMG_1755.JPG" \
#     --watermark_text "          Bếp Cô Vy\nTận tâm từng chiếc bánh" \
#     --font_name "TheNautigal" \
#     --font_size 150 \
#     --debug 1 \
#     --has_gui 0 \
#     --gimp_path "/Applications/GIMP-2.10.app/Contents/MacOS/gimp"

# python3 -B add_watermark.py --images_dir "/Users/${xxx}/Downloads/canon" \
#     --debug_image "3d83a3ef7d22b17ce833.jpg" \
#     --watermark_text "          Bếp Cô Vy\nTận tâm từng chiếc bánh" \
#     --font_name "FleurDeLeah" \
#     --font_size 12 \
#     --debug 1 \
#     --has_gui 0 \
#     --gimp_path "/Applications/GIMP-2.10.app/Contents/MacOS/gimp"

#FleurDeLeah
#TheNautigal
