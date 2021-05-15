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
        # adding atribute to config
        for key1 in self.data.data:
            for key2 in self.data.data[key1]:
                setattr(self, key1+"_"+key2, self.data.data[key1][key2])

    def get(self, key, sub_key):
        return self.data.data[key][sub_key]

    def set(self, key, sub_key, value):
        self.data[key][sub_key] = value

    def save(self):
        with open(self.config_file, "w") as f:
            f.write(self.data.as_yaml())


c = Config('config.yaml')
# # c.set("api", "url", "test")
# for attr, value in vars(c.data.data).items():
#     print(attr, value)
# for key1 in c.data.data:
#     for key2 in c.data.data[key1]:
#         setattr(c, key1+"_"+key2, c.data.data[key1][key2])

print(c.api_url)
# print(c.get("api", "url"))
