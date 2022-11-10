import json
import csv
import matplotlib.pyplot as plt
import numpy as np

# i plot name of field with it's value, because those values are unsorted, and they mix if i don't do it

def get_weapon_accuracy():
    with open('processed_data.json') as f:
        data = json.loads(f.read())
    del data[-1] # remove taser, as it doesn't have "hits" property
    accuracy =  [(val["name"], int(val["hits"])*100/int(val["shots"])) for val in data]
    return accuracy

def get_weapon_firing_speed():
    with open('csgo_weapons_stats.csv') as f:
        csvFile = list( csv.DictReader(f) )
    firing_speed = [ (val["Name"].lower(), float(val["Fire Rate (RPM)"])) for val in csvFile if '(' not in val["Name"]]
    return firing_speed

def generate_plot_data():
        accuracy = get_weapon_accuracy()
        firing_speed = get_weapon_firing_speed()
        return [( w, a, f ) for (w, a) in accuracy for (n, f) in firing_speed if w == n]

def plot_values(data):
    names, accuracy, firing_speed = zip(*data)
    firing_speed = np.array(firing_speed) * 100/max(firing_speed)

    a = 0.6
    plt.bar(names, accuracy, color='red', alpha=a, label = 'accuracy %')
    plt.bar(names, firing_speed, color='blue', alpha=a, label = 'normalized firing speed')

def setup_plot():
    plt.legend(loc="upper left")
    plt.xticks(rotation = 70)

def main():
    data = generate_plot_data()
    setup_plot()
    plot_values(data)
    plt.show()

if __name__ == "__main__":
    main()
