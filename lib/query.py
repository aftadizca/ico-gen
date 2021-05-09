import math
import pathlib
import json
import urllib.request
import requests
from lib.params import animation, cwd, cfg


def getImg(title, path):
    vars = {"search": title}
    response = requests.post(
        cfg.get("api", "url"),
        json={"query": cfg.get("api", "query"), "variables": vars}
    )

    json_data = json.loads(response.text)
    img_url = json_data["data"]["Media"]["coverImage"]["extraLarge"]

    # start request
    req = urllib.request.Request(
        img_url, headers={"User-Agent": "Mozilla/5.0"})
    opener = urllib.request.urlopen(req)
    length = opener.getheader("Content-Length")
    # initialize reading blocksize
    if length:
        length = int(length)
        blocksize = max(4096, math.ceil(length / 10))
    else:
        blocksize = 1000000  # just made something up
    # create buffer
    # buf = io.BytesIO()
    size = 0
    # read data and write to buffer
    with open(path, "ab") as f:
        while True:
            buf1 = opener.read(blocksize)
            if not buf1:
                break
            # buf.write(buf1)
            size += len(buf1)
            f.write(buf1)
            print(
                "\r ☕ {0:<70} {1:>15} {2:6}KB".format(
                    str(pathlib.Path(path).parent),
                    animation[round(size / length * 10) - 1], round(size/1000)
                ),
                flush=True,
                end="",
            )
        print()

    return img_url
