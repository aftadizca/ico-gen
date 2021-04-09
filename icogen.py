#!.pyenv/shims/python
from PIL import Image
import os
import pathlib
from query import getImg
from params import animation

pattern = (".jpg", ".png")
cwd = pathlib.Path(os.path.realpath(__file__)).parent
dir_anime = "/mnt/d/KOLEKSI/NEWANIME"
top_img = os.path.join(cwd, "top.png")
bottom_img = os.path.join(cwd, "bottom.png")


def icon_generator(top_img, img_target, bottom_img):
    images = [Image.open(x) for x in [top_img, img_target, bottom_img]]
    middle_img = images[1].resize((149, 211), Image.LANCZOS)
    new_img = Image.new("RGBA", (256, 256))
    new_img.paste(images[2])
    new_img.paste(middle_img, (31, 16))

    alphaComposite = Image.alpha_composite(new_img, images[0])
    alphaComposite.save(os.path.join(pathlib.Path(img_target).parent, "a.ico"))


for root, dirs, files in os.walk(dir_anime):
    for folder_name in dirs:
        if folder_name == "1. new":
            continue
        else:
            img_target = os.path.join(root, folder_name, "icon.jpg")
            if os.path.isfile(img_target):
                icon_generator(top_img, img_target, bottom_img)
                print(
                    "\r [♥]{0:<70} {1:15}".format(
                        os.path.join(root, folder_name),
                        animation[9],
                    ),
                    flush=True,
                    end="",
                )
                print()
            else:
                getImg(folder_name, img_target)
                icon_generator(top_img, img_target, bottom_img)
                # print(f"-{os.path.join(root, folder_name):<70} \tDone")