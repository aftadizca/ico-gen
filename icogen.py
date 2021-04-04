from PIL import Image


images = [Image.open(x) for x in ["top.png", "test.jpg", "bottom.png"]]

new_img = Image.new("RGBA", (256, 256))
