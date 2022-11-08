class weapon:
    def __init__(self, name, shots, hits, kills):
        self.name = name
        self.shots = shots
        self.hits = hits
        self.kills = kills

    def create_dict(self):
        return vars(self)

    def __str__(self):
        return f"n: {self.name} - s: {self.shots} - h: {self.hits} - k: {self.kills}"

def gather_weapons_data(data: dict, weapons_list):
    "this function reads data, and saves informations about each weapon"
    weapons = []
    for weapon_name in weapons_list:
        name, shots, hits, kills = "", 0, 0, 0
        for record in data["playerstats"]["stats"]:
            name = record["name"]
            if weapon_name in name:
                if "kills" in name:
                    kills = record["value"]
                    continue
                if "shots" in name:
                    shots = record["value"]
                    continue
                if "hits" in name:
                    hits = record["value"]
                    continue
        weapons.append(weapon(weapon_name, shots, hits, kills))
    return weapons
