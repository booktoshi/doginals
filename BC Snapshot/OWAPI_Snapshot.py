import requests
import json

def get_inscription_data(inscription_id):
    # API URL for fetching the outpoint and address
    outpoint_url = f"https://dogeturbo.ordinalswallet.com/inscription/{inscription_id}/outpoint"
    # API URL for fetching the name
    name_url = f"https://dogeturbo.ordinalswallet.com/inscription/{inscription_id}"
    
    # Fetching the data
    outpoint_response = requests.get(outpoint_url)
    name_response = requests.get(name_url)
    
    if outpoint_response.ok and name_response.ok:
        outpoint_data = outpoint_response.json()
        name_data = name_response.json()

        # Extract the address and name
        address = outpoint_data.get('inscription', {}).get('address', 'Not Found')
        name = name_data.get('meta', {}).get('name', 'Not Found')

        return {
            'id': inscription_id,
            'address': address,
            'name': name
        }
    else:
        return None

def process_inscriptions(file_path):
    # Load the JSON data from file
    with open(file_path, 'r') as file:
        inscriptions = json.load(file)
    
    results = []
    total = len(inscriptions)
    for index, inscription in enumerate(inscriptions):
        inscription_id = inscription['id']
        data = get_inscription_data(inscription_id)
        if data:
            results.append(data)
        time.sleep(1)
        
        # Print progress
        print(f"Progress: {((index + 1) / total) * 100:.2f}%")

    # Save the results to a new JSON file
    with open('output_results.json', 'w') as file:
        json.dump(results, file, indent=4)

# Replace 'OW.json' with the path to your JSON file if it's different
process_inscriptions('OW.json')
