import json
from weapon import gather_weapons_data
from sys import argv
import pathlib

def get_weapon_names(data):
    "this function returns an array of weapon names"
    weapon_names = [el["name"][12:] for el in data["playerstats"]["stats"] if "total_shots_" in el["name"]]
    weapon_names.remove('hit')
    weapon_names.remove('fired')
    return weapon_names

def main():
    # at this point i assume i receive correct data
    data_file = "data.json"
    if len(argv) != 1:
        _, data_file = argv
    elif not pathlib.Path("data.json").is_file():
        exit("None data file provided")

    with open(data_file) as file:
        data = json.loads(file.read())

    weapon_names = get_weapon_names(data)
    weapons = gather_weapons_data(data, weapon_names)
    try:
        with open('processed_data.json', 'w') as file:
            result_json=json.dumps( [weapon.create_dict() for weapon in weapons], indent=4 )
            file.write(result_json)
    except PermissionError:
        exit("You have no permissions to save files in this directory")
    except:
        exit("An unknown error occured")

if __name__ == "__main__":
    main()
