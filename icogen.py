from PIL import Image


images = [Image.open(x) for x in ["top.png", "test.jpg", "bottom.png"]]

middle_img = images[1].resize((149, 211))

new_img = Image.new("RGBA", (256, 256))

new_img.paste(images[2])
new_img.paste(middle_img, (31, 16))
new_img.paste(images[0], (0, 0), images[0])

new_img.save("res.ico")
