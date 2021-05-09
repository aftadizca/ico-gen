import pathlib
import os
import toml
from strictyaml import load, Map, Str, Seq


class Config:
    def __init__(self, config_file):
        # yaml schema
        schema = Map({"api": Map({"url": Str(), "query": Str()}),
                      "dir": Map({"anime": Str(), "exclude": Seq(Str())})})
        # open yaml file and load
        self.config_file = config_file
        with open(config_file, "r", encoding="utf8") as f:
            self.data = load(f.read(), schema)

    def get(self, key, sub_key):
        return self.data.data[key][sub_key]

    def set(self, key, sub_key, value):
        self.data[key][sub_key] = value

    def save(self):
        with open(self.config_file, "w") as f:
            f.write(self.data.as_yaml())


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

cwd = pathlib.Path(os.path.realpath(__file__)).parent.parent
top_img = os.path.join(cwd, "img/top.png")
bottom_img = os.path.join(cwd, "img/bottom.png")
cfg_file = os.path.join(cwd, "config.yaml")

cfg = Config(cfg_file)
