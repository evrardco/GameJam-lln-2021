import json
from os.path import join
from src.globals import HEIGHT


class ObjectParser:
    def __init__(self, name):
        self.root = None
        with open(join("assets", "maps", f"{name}.json"), "r") as f:
            self.root = json.load(f)
        for l in self.root["layers"]:
            if l["name"] == "path_finding":
                #filter the objects and apply Y-Offset correction
                objects = [{
                    "name":o["name"],
                    "x":o["x"],
                    "y": HEIGHT - o["y"],
                    "turn_dir":o["properties"][0]["value"]
                    } for o in l["objects"]]
                self.path_finding = sorted(objects, key=lambda x: int(x["name"]))
                # print(self.path_finding)
                
            elif l["name"] == "tower_spots":
                self.tower_spots = l["objects"]


            elif l["name"] == "game_info":
                for o in l["objects"]:
                    if o["name"] == "waves":
                        for p in o["properties"]:
                            if p["name"] == "json":
                                self.waves = json.loads(p["value"])

                    elif o["name"] == "game_values":
                        for p in o["properties"]:
                            if p["name"] == "json":
                                temp = json.loads(p["value"])
                                self.followers = int(temp["followers"])
                                self.max_votes = int(temp["max_votes"])
                
