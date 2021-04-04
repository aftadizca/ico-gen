from PIL import Image
import os
import fnmatch

dir_anime = "/mnt/d/KOLEKSI/NEWANIME"
pattern = (".jpg", ".png")


for root, _, files in os.walk(dir_anime):
    for filename in files:
        if filename.endswith((".jpg", ".png")):
            img_target = os.path.join(root, filename)
            print(" - " + root)
            images = [Image.open(x) for x in ["top.png", img_target, "bottom.png"]]

            middle_img = images[1].resize((149, 211))

            new_img = Image.new("RGBA", (256, 256))

            new_img.paste(images[2])
            new_img.paste(middle_img, (31, 16))
            new_img.paste(images[0], (0, 0), images[0])

            new_img.save(os.path.join(root, "a.ico"))
