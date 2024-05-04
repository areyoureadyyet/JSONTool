import json

def get_data(filename : str, data_tag : str):
    json_code = open(filename, 'r')
    data = json_code.read()
    json_code.close()
    data = json.loads(data)
    return data[data_tag]

def convert_to_json(filename, dict : dict):
    file = open(filename, 'w')
    file.write(json.dumps(dict))
    file.close()



