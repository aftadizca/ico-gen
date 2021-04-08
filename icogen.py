#!.pyenv/shims/python
from PIL import Image
import os
import pathlib

pattern = (".jpg", ".png")
cwd = pathlib.Path(os.path.realpath(__file__)).parent
dir_anime = "/mnt/d/KOLEKSI/NEWANIME"
top_img = os.path.join(cwd, "top.png")
bottom_img = os.path.join(cwd, "bottom.png")

for root, _, files in os.walk(dir_anime):
    for filename in files:
        if filename.endswith(pattern):
            img_target = os.path.join(root, filename)
            print(" - " + root)
            images = [Image.open(x) for x in [top_img, img_target, bottom_img]]

            middle_img = images[1].resize((149, 211), Image.LANCZOS)

            new_img = Image.new("RGBA", (256, 256))

            new_img.paste(images[2])
            new_img.paste(middle_img, (31, 16))

            alphaComposite = Image.alpha_composite(new_img, images[0])
            alphaComposite.save(os.path.join(root, "a.ico"))

            # new_img.paste(images[0], images[0])

            # new_img.save(os.path.join(root, "a.ico"))
