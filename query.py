import io, math, pathlib, os, json, urllib.request, requests
from params import animation, cwd

url = "https://graphql.anilist.co"
query = """query ($search: String){
  Media(search: $search, type:ANIME) {
    id
    coverImage {
      extraLarge
    }
    title {
      romaji
    }
  }
}"""


def getImg(title, path):
    vars = {"search": title}
    response = requests.post(url, json={"query": query, "variables": vars})
    json_data = json.loads(response.text)
    img_url = json_data["data"]["Media"]["coverImage"]["extraLarge"]

    # start request
    req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
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
                "\r [♥]{0:<70} {1:15}".format(
                    str(pathlib.Path(path).parent),
                    animation[round(size / length * 10) - 1],
                ),
                flush=True,
                end="",
            )
        print()

    return img_url


# getImg("OreImo", os.path.join(cwd, "test.jpg"))
