import json
import re

def extract_number_from_filename(filename):
    """ Extract the numeric part from the filename and convert it to an integer. """
    match = re.search(r'(\d+)\.html$', filename)
    return int(match.group(1)) if match else None

# Read the original JSON file
with open('autoInscriberOutput.json', 'r') as file:
    data = json.load(file)

# Transform the data
transformed_data = []
for key, value in data.items():
    number = extract_number_from_filename(key)
    if number is not None:
        transformed_entry = {
            "id": value + "i0",
            "meta": {
                "name": f"Collection name #{number}"
            }
        }
        transformed_data.append(transformed_entry)

# Write the transformed data to a new JSON file
with open('OWcollection.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)

print("Transformation complete. Data saved in OWcollection.json")
