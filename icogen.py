#!/usr/bin/env python
from PIL import Image
import os
import pathlib
import argparse
from lib.query import getImg
from lib.params import animation, cwd, top_img, bottom_img, cfg, cfg_file


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
sub_parser = parser.add_subparsers(help="Sub Command Help", dest="name")
init_parser = sub_parser.add_parser("start", help="Start make folder icon")
init_parser.add_argument('-f', '--force', action='store_true',
                         help="Force to redownload icon image")

set_parser = sub_parser.add_parser("set", help="Start make folder icon")
set_parser.add_argument('-d', '--dir', type=str, action='store', default=None,
                        help="Set anime dir location")
set_parser.add_argument('-e', '--exclude', nargs="*", action='store', default=None,
                        help="Set exluded folder in anime dir location")

args = parser.parse_args(["start"])
print(args)

if args.name == "start":
    for root, dirs, files in os.walk(cfg.get("dir", "anime")):
        for exclude in cfg.get("dir", "exclude"):
            try:
                dirs.remove(exclude)
            except ValueError:
                pass
        for folder_name in dirs:
            img_target = os.path.join(root, folder_name, "icon.jpg")
            if os.path.isfile(img_target) and not args.force:
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
        break  # disable recursive
if args.name == "set":
    if args.dir:
        cfg.set("dir", "anime", args.dir)
        cfg.save()
    elif args.exclude:
        cfg.set("dir", "exclude", args.exclude)
        cfg.save()
