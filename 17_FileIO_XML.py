'''
Task:

    1. Parsing XML Data:
        * Read the provided XML file (data.xml) using ElementTree.
        * Extract the following information from the XML:
                Name of the book.
                Author of the book.
                Publication year of the book.
                Price of the book.
                List of genres the book belongs to (if available).
        * Print the extracted information.

    2. Adding New Book:
        * Create a new book entry with the following details:
                Name: "Python Programming"
                Author: "Guido van Rossum"
                Publication Year: 2022
                Price: $39.99
                Genre: "Programming"
        * Add the new book entry to the existing XML structure.

    3. Writing XML Data:
        * Write the modified XML data back to a new XML file (updated_data.xml).
        * Ensure the XML file maintains the same structure as the original file, with the addition of the new book entry.

Instructions:

    * Use Python's ElementTree module to parse and manipulate XML data.
    * Ensure proper error handling is implemented for file operations and XML parsing.
    * Use meaningful variable names and comments to enhance code readability.
    * Submit both the Python script and the updated XML file (updated_data.xml).
    * Include any additional documentation or explanation as needed in the script.

Note:
Ensure that the provided XML file (data.xml) contains at least one book entry to facilitate the parsing and modification tasks.
'''


import xml.etree.ElementTree as ET

# Parsing XML Data
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        price = book.find('price').text
        genres = [genre.text for genre in book.find('genres').findall('genre')]

        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Year: {year}")
        print(f"Price: {price}")
        print(f"Genres: {', '.join(genres)}\n")

# Adding New Book
def add_new_book(file_path, new_book_data):
    tree = ET.parse(file_path)
    root = tree.getroot()

    new_book = ET.Element('book')
    ET.SubElement(new_book, 'title').text = new_book_data['title']
    ET.SubElement(new_book, 'author').text = new_book_data['author']
    ET.SubElement(new_book, 'year').text = str(new_book_data['year'])
    ET.SubElement(new_book, 'price').text = str(new_book_data['price'])
    
    genres = ET.SubElement(new_book, 'genres')
    ET.SubElement(genres, 'genre').text = new_book_data['genre']

    root.append(new_book)
    tree.write('updated_data.xml')

if __name__ == "__main__":
    # Path to the XML file
    xml_file_path = 'data.xml'
    
    # Parsing the XML file and printing the contents
    parse_xml(xml_file_path)
    
    # New book data to be added
    new_book = {
        'title': 'Python Programming',
        'author': 'Guido van Rossum',
        'year': 2022,
        'price': 39.99,
        'genre': 'Programming'
    }
    
    # Adding the new book and writing to a new file
    add_new_book(xml_file_path, new_book)
