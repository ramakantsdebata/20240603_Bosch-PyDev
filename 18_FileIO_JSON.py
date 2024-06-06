'''
Task:

    1. Parsing JSON Data:
        * Read the provided JSON file (data.json) using the json module.
        * Extract the following information from the JSON:
                Name of the product.
                Category of the product.
                Price of the product.
                Availability of the product.
        * Print the extracted information.

    2. Adding New Product:
        * Create a new product entry with the following details:
                Name: "Python Programming Book"
                Category: "Books"
                Price: $39.99
                Availability: true
        * Add the new product entry to the existing JSON structure.

    3. Writing JSON Data:
        * Write the modified JSON data back to a new JSON file (updated_data.json).
        * Ensure the JSON file maintains the same structure as the original file, with the addition of the new product entry.

Instructions:

    * Use Python's json module to parse and manipulate JSON data.
    * Ensure proper error handling is implemented for file operations and JSON parsing.
    * Use meaningful variable names and comments to enhance code readability.
    * Submit both the Python script and the updated JSON file (updated_data.json).
    * Include any additional documentation or explanation as needed in the script.

Note:
Ensure that the provided JSON file (data.json) contains at least one product entry to facilitate the parsing and modification tasks.
'''


import json

# Parsing JSON Data
def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        for product in data:
            name = product.get('name')
            category = product.get('category')
            price = product.get('price')
            availability = product.get('availability')
            
            print(f"Name: {name}")
            print(f"Category: {category}")
            print(f"Price: {price}")
            print(f"Availability: {availability}\n")

# Adding New Product
def add_new_product(file_path, new_product_data):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    data.append(new_product_data)
    
    with open('updated_data.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # Path to the JSON file
    json_file_path = 'data.json'
    
    # Parsing the JSON file and printing the contents
    parse_json(json_file_path)
    
    # New product data to be added
    new_product = {
        "name": "Python Programming Book",
        "category": "Books",
        "price": 39.99,
        "availability": True
    }
    
    # Adding the new product and writing to a new file
    add_new_product(json_file_path, new_product)
