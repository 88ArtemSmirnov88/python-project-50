from gendiff.formats.formatter import get_format
from gendiff.parse import parse


def generate_diff(file_path1, file_path2, format):
    data1, ext1 = get_data_file(file_path1)
    data2, ext2 = get_data_file(file_path2)
    tree = builder_tree(parse(data1, ext1), parse(data2, ext2))
    return get_format(tree, format)


def get_data_file(path_file):
    ext = path_file.split('.')[1]
    with open(path_file) as f:
        data = f.read()
        return data, ext


def builder_tree(data1, data2):
    keys = sorted(list(data1.keys() | data2.keys()))
    result = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1:
            children = {
                'type': 'added',
                'key': key,
                'value': value2
            }
        elif key not in data2:
            children = {
                'type': 'deleted',
                'key': key,
                'value': value1
            }
        elif data1[key] == data2[key]:
            children = {
                'type': 'unchanged',
                'key': key,
                'value': value2
            }
        elif isinstance(data1[key], dict) and isinstance(
                data2[key], dict):
            children = {
                'type': 'nested',
                'key': key,
                'value': builder_tree(value1, value2)
            }
        else:
            children = {
                'type': 'changed',
                'key': key,
                'value': value1,
                'value2': value2
            }
        result.append(children)
    return result
