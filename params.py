import pathlib, os

animation = [
    "[♥♡♡♡♡♡♡♡♡♡]",
    "[♥♥♡♡♡♡♡♡♡♡]",
    "[♥♥♥♡♡♡♡♡♡♡]",
    "[♥♥♥♥♡♡♡♡♡♡]",
    "[♥♥♥♥♥♡♡♡♡♡]",
    "[♥♥♥♥♥♥♡♡♡♡]",
    "[♥♥♥♥♥♥♥♡♡♡]",
    "[♥♥♥♥♥♥♥♥♡♡]",
    "[♥♥♥♥♥♥♥♥♥♡]",
    "[♥♥♥♥♥♥♥♥♥♥]",
]

cwd = pathlib.Path(os.path.realpath(__file__)).parent
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
