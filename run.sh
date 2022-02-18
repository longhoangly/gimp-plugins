#!/bin/zsh

echo
echo Starting add watermark process...

# [Image + No Debug]
# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
#     --watermark_path "/Users/long.lyhoang/Downloads/Bep Co Vy/Watermark-4.png" \
#     --debug_image "IMG_1755.JPG" \
#     --has_gui 1

# [Image + Debug]
python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
    --watermark_path "/Users/long.lyhoang/Downloads/Bep Co Vy/Watermark-4.png" \
    --debug_image "IMG_1755.JPG" \
    --debug 1 \
    --has_gui 1

# [Text + No Debug]
# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
#     --watermark_text "Bếp Cô Vy...Ahihi..." \
#     --font_name "Sans" \
#     --font_size 30 \
#     --has_gui 1

# [Text + Debug]
# python3 -B add_watermark.py --images_dir "/Users/long.lyhoang/Downloads/Bep Co Vy/2022_02_16" \
#     --debug_image "IMG_1755.JPG" \
#     --watermark_text "Bếp Cô Vy...Ahihi..." \
#     --font_name "Sans" \
#     --font_size 30 \
#     --debug 1 \
#     --has_gui 1
