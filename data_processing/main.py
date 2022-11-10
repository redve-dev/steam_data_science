import json
import csv
import matplotlib.pyplot as plt

def weapon_accuracy_plot(weapons, data):
    del data[-1] # remove taser, as it doesn't have "hits" property
    accuracy = [val["hits"]*100/val["shots"] for val in data]
    weapons, accuracy = zip(*sorted(zip(weapons, accuracy)))
    return accuracy

def weapon_firerate_plot(weapons):
    with open('csgo_weapons_stats.csv') as f:
        csvFile = list( csv.DictReader(f) )
    firing_speed = [val["Fire Rate (RPM)"] for val in csvFile if '(' not in val["Name"]]
    weapons, firing_speed = zip(*sorted(zip(weapons, firing_speed)))
    return firing_speed

def main():
    with open('processed_data.json') as f:
        data = json.loads(f.read())

    weapons = sorted([val["name"].lower() for val in data])
    weapons.remove('taser')
    accuracy = weapon_accuracy_plot(weapons, data)
    firing_speed = weapon_firerate_plot(weapons)
    print(len(accuracy))
    print(len(firing_speed))
    print(len(weapons))
    plt.bar(weapons, accuracy, color='blue', alpha=0.5)
    plt.bar(weapons, firing_speed, color='red', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    main()
