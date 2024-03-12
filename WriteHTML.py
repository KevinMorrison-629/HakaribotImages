

import os
import sys




BASE_HTML = ""
with open("BASE_IMAGE_HTML.html", "r") as f:
    BASE_HTML = f.read()


if "html" not in os.listdir():
    os.mkdir("html")



images = os.listdir("images")


for src in os.listdir("images"):
    dst = src.replace("PORTRAIT_","").replace(" ","_")
    os.rename(f"images/{src}",f"images/{dst}")



for img in os.listdir("images"):
    htmlFilename = img.replace(".jpg","")
    with open(f"html\\{htmlFilename}.html", "w", encoding="utf-8") as f:
        NAME, INDEX, temp = img.rsplit("_",maxsplit=2)
        charHtml = BASE_HTML.replace("IMAGE_NAME", "images/" + img).replace("CHARACTER_NAME", NAME)
        f.write(charHtml)
