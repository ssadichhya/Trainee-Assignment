import json


def add_to_json(filename, new_data):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)

        existing_data.append(new_data)

        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=2)

        print(f"New data added successfully to '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON data in '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


new_dict = {
    "name": "sadichhya",
    "age": 23
}

filename = "sample.json"
add_to_json(filename, new_dict)
