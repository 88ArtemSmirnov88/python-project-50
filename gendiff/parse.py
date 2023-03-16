import json
import yaml


def parse(file):
    if file.startswith('{') or file.startswith('['):
        result = json.loads(file)
    else:
        result = yaml.safe_load(file)
    return result
