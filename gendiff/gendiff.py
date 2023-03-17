from gendiff.formats.get_formats import get_format
from gendiff.formats.formatter import unify_values
from gendiff.parse import parse


def generate_diff(first_file, second_file, format='stylish'):
    with open(first_file, 'r') as f1, open(second_file, 'r') as f2:
        file1 = f1.read()
        file2 = f2.read()
    result = builder_tree(parse(file1), parse(file2))
    return get_format(format, result)


def builder_tree(data1, data2):
    keys = sorted(list(data1.keys() | data2.keys()))
    result = []
    for key in keys:
        value1 = unify_values(data1.get(key))
        value2 = unify_values(data2.get(key))
        if key not in data1:
            children = {
                'type': 'ADDED',
                'key': key,
                'value': value2
            }
        elif key not in data2:
            children = {
                'type': 'DELETED',
                'key': key,
                'value': value1
            }
        elif data1[key] == data2[key]:
            children = {
                'type': 'UNCHANGED',
                'key': key,
                'value': value2
            }
        elif isinstance(data1[key], dict) and isinstance(
                data2[key], dict):
            children = {
                'type': 'NESTED',
                'key': key,
                'value': builder_tree(value1, value2)
            }
        else:
            children = {
                'type': 'CHANGED',
                'key': key,
                'value': value1,
                'value2': value2
            }
        result.append(children)
    return result
