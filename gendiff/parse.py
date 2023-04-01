import json
import yaml


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    if extension == 'yaml':
        return yaml.safe_load(data)
    return Exception(f'Unknown format: {extension}')
