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
                self.waves = []
                for o in l["objects"]:
                    if o["name"].beginswith("wave_"):
                        for p in o["properties"]:
                            if p["name"] == "json":
                                self.waves.append(json.loads(p))
                                


