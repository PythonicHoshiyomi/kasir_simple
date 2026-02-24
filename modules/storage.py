import json

FILE_NAME = "riwayat.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(data):
    existing_data = load_data()
    existing_data.append(data)
    with open(FILE_NAME, "w") as file:
        json.dump(existing_data, file, indent=4)
