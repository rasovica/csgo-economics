class Skin:
    def __init__(self, skin):
        self.name = skin["name"]
        self.exterior = skin.get("exterior")

        if skin.get("price"):
            price = skin["price"].get("7_days") or skin["price"].get("30_days") or skin["price"].get("all_time")
            self.average_price = price["average"]
            self.median_price = price["median"]
            self.volume = int(price["sold"] if price["sold"] != "" else "0")
            self.std = float(price["standard_deviation"])
            self.lowest_price = price["lowest_price"]
            self.highest_price = price["highest_price"]
