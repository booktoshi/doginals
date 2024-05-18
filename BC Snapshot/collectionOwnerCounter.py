import json

# Function to read JSON data
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to count occurrences of each address
def count_addresses(data):
    address_counts = {}
    for item in data:
        address = item['address']
        if address in address_counts:
            address_counts[address] += 1
        else:
            address_counts[address] = 1
    return address_counts

# Function to write data to a JSON file
def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Main function
def main():
    input_file = 'output_results.json'
    output_file = 'AddressCounts.json'

    # Read data from the output JSON file
    scraped_data = read_json_file(input_file)

    # Count the occurrences of each address
    address_counts = count_addresses(scraped_data)

    # Create a list to store the formatted data
    formatted_data = [{'address': address, 'count': count} for address, count in address_counts.items()]

    # Write the formatted data to a new JSON file
    write_json_file(output_file, formatted_data)

    print("Address count data saved to AddressCounts.json")

if __name__ == '__main__':
    main()
