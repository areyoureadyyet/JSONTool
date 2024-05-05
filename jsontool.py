import json

def get_data(filename: str, data_tag: str, data_tag_count: int):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            if data_tag in data:  # Check if the data_tag exists in the JSON data
                return data[data_tag][:data_tag_count]  # Return the specified number of elements
            else:
                print(f"Data tag '{data_tag}' not found in JSON data.")
                return None
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return None

def convert_to_json(filename: str, data_dict: dict):
    try:
        with open(filename, 'w') as file:
            json.dump(data_dict, file)
    except IOError:
        print("Error writing to file.")

# Example usage
# data = get_data('data.json', 'cars', 2)
# if data:
#     print(data)

# # Example conversion
# data_dict = {'name': 'Mr.X', 'cars': [{'model': 'Audi'}, {'model': 'Ferrari'}]}
# convert_to_json('output.json', data_dict)




