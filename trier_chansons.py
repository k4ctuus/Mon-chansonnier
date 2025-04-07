import json

with open('chansons.json', 'r') as file:
    chansons = json.load(file)

chansons_sorted = sorted(chansons, key=lambda x: x['titre'])

with open('chansons_sorted.json', 'w') as file:
    json.dump(chansons_sorted, file, indent=4)
