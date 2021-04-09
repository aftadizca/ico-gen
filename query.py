import requests
import json
import urllib.request
import os
import pathlib

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

cwd = pathlib.Path(os.path.realpath(__file__)).parent


def getImg(title, path):
    vars = {"search": title}
    response = requests.post(url, json={"query": query, "variables": vars})
    json_data = json.loads(response.text)
    img_url = json_data["data"]["Media"]["coverImage"]["extraLarge"]

    req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
    opener = urllib.request.urlopen(req)
    with open(path, "b+w") as f:
        f.write(opener.read())

    return img_url
