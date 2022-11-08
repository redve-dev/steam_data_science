import json
from weapon import gather_weapons_data
from sys import argv
import pathlib

def main():
    data_file = "data.json"
    if len(argv) != 1:
        _, data_file = argv
    elif not pathlib.Path("data.json").is_file():
        exit("None data file provided")

    with open(data_file) as file:
        data = json.loads(file.read())
        weapon_names = []
        for el in data["playerstats"]["stats"]:
            if "total_shots_" in el["name"]:
                weapon_names.append(el["name"][12:])
        weapon_names.remove('hit')
        weapon_names.remove('fired')
        weapons = gather_weapons_data(data, weapon_names)
        for el in weapons:
            print(el)

if __name__ == "__main__":
    main()
