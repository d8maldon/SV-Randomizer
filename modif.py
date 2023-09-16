import json

# Load the JSON file
with open('code.json', 'r') as file:
    data = json.load(file)

# Iterate through each entry and set evo_data level to 1
for entry in data['entry']:
    if not entry['evo_data']:
        entry['evo_data'].append({"level": 1})
    else:
        for evo_data_entry in entry['evo_data']:
            evo_data_entry['level'] = 1

# Write the updated JSON back to the file
with open('code.json', 'w') as file:
    json.dump(data, file, indent=2)

