import json
from os.path import join
class ObjectParser:
    def __init__(self, name):
        self.root = None
        with open(join("assets", "maps", f"{name}.json"), "r") as f:
            self.root = json.load(f)
        for l in self.root["layers"]:
            if l["name"] == "path_finding":
                self.path_finding = sorted(l["objects"], key=lambda x: int(x["name"]))
            if l["name"] == "tower_spots":
                self.tower_spots = l["objects"]

