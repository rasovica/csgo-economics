import DataLoader
import json

data_loader = DataLoader.DataLoader()
skins = data_loader.load_skins()

db = {
    "skins": [skin.__dict__ for skin in skins],
}

with open("db.json", "w+") as file:
    json.dump(db, file)
