#17. **Läs XML-data:** Implementera ett program som kan läsa och extrahera data från en XML-fil.

import xml.etree.ElementTree as ET

def read_xml(file_path):
    try:
        # Parse XML-filen
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Extrahera data från XML
        for person in root.findall('person'):
            name = person.find('name').text
            age = person.find('age').text
            city = person.find('city').text
            
            print(f"Name: {name}, Age: {age}, City: {city}")
    except FileNotFoundError:
        print("Filen hittades inte. Kontrollera filvägen.")
    except ET.ParseError:
        print("Fel vid parsning av XML-filen.")
    except Exception as e:
        print(f"Ett oväntat fel inträffade: {e}")

# Ange filvägen till din XML-fil
file_path = "data.xml"
read_xml(file_path)
