import pathlib
import os
import toml

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
cfg_file = os.path.join(cwd, "config.toml")

with open(cfg_file, 'r') as f:
    cfg = toml.load(f)
