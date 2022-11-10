import json
import csv
import matplotlib.pyplot as plt

def weapon_accuracy_plot(data):
    del data[-1] # remove taser, as it doesn't have "hits" property
    weapons = [val["name"] for val in data]
    accuracy = [val["hits"]*100/val["shots"] for val in data]
    plt.title('average accuracy per weapon')
    _,labels = plt.xticks()
    plt.setp(labels, rotation=70)
    plt.bar(weapons, accuracy)

def weapon_firerate_plot():
    with open('csgo_weapons_stats.csv') as f:
        csvFile = list( csv.DictReader(f) )
    weapons = [val["Name"] for val in csvFile if '(' not in val["Name"]]
    firing_speed = [val["Fire Rate (RPM)"] for val in csvFile if '(' not in val["Name"]]
    plt.bar(weapons, firing_speed, color='pink')
    

def main():
    with open('processed_data.json') as f:
        data = json.loads(f.read())

    weapon_firerate_plot()
    # weapon_accuracy_plot(data)
    plt.show()

if __name__ == "__main__":
    main()
