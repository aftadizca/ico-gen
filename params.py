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

cwd = pathlib.Path(os.path.realpath(__file__)).parent
top_img = os.path.join(cwd, "img/top.png")
bottom_img = os.path.join(cwd, "img/bottom.png")

with open(os.path.join(cwd, "config.toml"), 'r') as f:
    cfg = toml.load(f)
