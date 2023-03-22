import requests
import Skin


class DataLoader:
    marketable_skins = list()

    def load_skins(self):
        res = requests.get("http://csgobackpack.net/api/GetItemsList/v2/?currency=eur").json()

        if not res["success"]:
            raise Exception("Server responded without success")

        self.marketable_skins = [Skin.Skin(item) for item in res["items_list"].values() if item["marketable"] == 1]

        return self.marketable_skins
