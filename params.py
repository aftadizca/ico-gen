import pathlib
import os

animation = [
    "[💚🖤🖤🖤🖤🖤🖤🖤🖤🖤]",
    "[💚💚🖤🖤🖤🖤🖤🖤🖤🖤]",
    "[💚💚💚🖤🖤🖤🖤🖤🖤🖤]",
    "[💚💚💚💚🖤🖤🖤🖤🖤🖤]",
    "[💚💚💚💚💚🖤🖤🖤🖤🖤]",
    "[💚💚💚💚💚💚🖤🖤🖤🖤]",
    "[💚💚💚💚💚💚💚🖤🖤🖤]",
    "[💚💚💚💚💚💚💚💚🖤🖤]",
    "[💚💚💚💚💚💚💚💚💚🖤]",
    "[💚💚💚💚💚💚💚💚💚💚]",
]

cwd = pathlib.Path(os.path.realpath(__file__)).parent
dir_anime = "/mnt/d/KOLEKSI/NEWANIME"
top_img = os.path.join(cwd, "top.png")
bottom_img = os.path.join(cwd, "bottom.png")

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
