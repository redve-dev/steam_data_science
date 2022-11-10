import json
import csv
import matplotlib.pyplot as plt

def get_weapon_accuracy():
    with open('processed_data.json') as f:
        data = json.loads(f.read())
    del data[-1] # remove taser, as it doesn't have "hits" property
    accuracy =  [(val["name"], val["hits"]*100/val["shots"]) for val in data]
    return accuracy

def get_weapon_firing_speed():
    with open('csgo_weapons_stats.csv') as f:
        csvFile = list( csv.DictReader(f) )
    firing_speed = [ (val["Name"].lower(), val["Fire Rate (RPM)"]) for val in csvFile if '(' not in val["Name"]]
    return firing_speed

def generate_plot_data():
        accuracy = get_weapon_accuracy()
        firing_speed = get_weapon_firing_speed()
        return [( w, a, f ) for (w, a) in accuracy for (n, f) in firing_speed if w == n]

def plot_values(data):
    pass

def main():
    data = generate_plot_data()
    plot_values(data)
    plt.show()

if __name__ == "__main__":
    main()
