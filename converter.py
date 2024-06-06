import json
import yaml
import xml.etree.ElementTree as ET

def load_json(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

def save_json(data, path):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Could not save JSON file: {e}")
        sys.exit(1)

def load_yaml(path):
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

def save_yaml(data, path):
    try:
        with open(path, 'w') as file:
            yaml.dump(data, file)
    except IOError as e:
        print(f"Could not save YAML file: {e}")
        sys.exit(1)

def load_xml(path):
    try:
        tree = ET.parse(path)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Invalid XML file: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)
