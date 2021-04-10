#!.pyenv/shims/python
from PIL import Image
import os
import pathlib
import time
import argparse
from query import getImg
from params import animation, cwd, top_img, bottom_img, dir_anime


def icon_generator(top_img, img_target, bottom_img):
    images = [Image.open(x) for x in [top_img, img_target, bottom_img]]
    middle_img = images[1].resize((149, 211), Image.LANCZOS)
    new_img = Image.new("RGBA", (256, 256))
    new_img.paste(images[2])
    new_img.paste(middle_img, (31, 16))

    alphaComposite = Image.alpha_composite(new_img, images[0])
    alphaComposite.save(os.path.join(pathlib.Path(img_target).parent, "a.ico"))


parser = argparse.ArgumentParser(
    description="Auto download cover from Anilist.co & make folder icon")
parser.add_argument('-f', '--force', dest='force',
                    action='store_false', help="Force to redownload icon image")
args = parser.parse_args()


for root, dirs, files in os.walk(dir_anime):
    for folder_name in dirs:
        if folder_name == "1. new":
            continue
        else:
            img_target = os.path.join(root, folder_name, "icon.jpg")
            if os.path.isfile(img_target) and args.force:
                icon_generator(top_img, img_target, bottom_img)
                print(
                    "\r ☕ {0:<70} {1:>5}".format(
                        os.path.join(root, folder_name),
                        "✅",
                    ),
                    flush=True,
                    end="",
                )
                print()
            else:
                getImg(folder_name, img_target)
                icon_generator(top_img, img_target, bottom_img)
                # print(f"-{os.path.join(root, folder_name):<70} \tDone")
