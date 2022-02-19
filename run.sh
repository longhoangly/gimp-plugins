#!/bin/zsh

echo
echo Starting add watermark process...

# [Image Watermark + No Debug]
# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
#     --watermark_path "/Users/long.lyhoang/Downloads/Bep Co Vy/Watermark-4.png" \
#     --debug_image "IMG_1755.JPG" \
#     --has_gui 1

# [Image Watermark + Debug]
# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
#     --watermark_path "/Users/long.lyhoang/Downloads/Bep Co Vy/Watermark-5.png" \
#     --debug_image "IMG_1755.JPG" \
#     --debug 1 \
#     --has_gui 1

# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy" \
#     --watermark_path "/Users/long.lyhoang/Downloads/Bep Co Vy/BepCoVy-1.png" \
#     --debug_image "3d83a3ef7d22b17ce833.jpg" \
#     --debug 1 \
#     --has_gui 1

# [Text Watermark + No Debug]
# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
#     --watermark_text "Bếp Cô Vy" \
#     --font_name "FleurDeLeah" \
#     --font_size 30 \
#     --has_gui 1

# [Text Watermark + Debug]
python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
    --debug_image "IMG_1755.JPG" \
    --watermark_text "          Bếp Cô Vy\nTận tâm từng chiếc bánh" \
    --font_name "TheNautigal" \
    --font_size 150 \
    --debug 1 \
    --has_gui 0

python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy" \
    --debug_image "3d83a3ef7d22b17ce833.jpg" \
    --watermark_text "          Bếp Cô Vy\nTận tâm từng chiếc bánh" \
    --font_name "FleurDeLeah" \
    --font_size 12 \
    --debug 1 \
    --has_gui 0

#FleurDeLeah
#TheNautigal
