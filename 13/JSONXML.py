#13. **Skapa ett program som konverterar JSON-data till en XML-fil och vice versa.**

import json
import xml.etree.ElementTree as ET

def json_to_xml(json_data, root_name="root"):
    """Konvertera JSON-data till XML-struktur."""
    def build_xml_element(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                build_xml_element(child, value)
        elif isinstance(data, list):
            for item in data:
                child = ET.SubElement(parent, "item")
                build_xml_element(child, item)
        else:
            parent.text = str(data)

    root = ET.Element(root_name)
    build_xml_element(root, json_data)
    return ET.tostring(root, encoding="unicode")

def xml_to_json(xml_data):
    """Konvertera XML-struktur till JSON-data."""
    def parse_element(element):
        if len(element) == 0:  # Om elementet inte har några barn
            return element.text
        return {child.tag: parse_element(child) for child in element}

    root = ET.fromstring(xml_data)
    return {root.tag: parse_element(root)}

# Exempel på användning
if __name__ == "__main__":
    # JSON till XML
    json_data = {
        "person": {
            "name": "Alice",
            "age": 30,
            "hobbies": ["reading", "cycling"]
        }
    }
    xml_result = json_to_xml(json_data, root_name="data")
    print("XML Result:")
    print(xml_result)

    # XML till JSON
    xml_data = """
<data>
    <person>
        <name>Alice</name>
        <age>30</age>
        <hobbies>
            <item>reading</item>
            <item>cycling</item>
        </hobbies>
    </person>
</data>
"""
    json_result = xml_to_json(xml_data)
    print("\nJSON Result:")
    print(json.dumps(json_result, indent=4))
