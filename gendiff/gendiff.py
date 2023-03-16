from gendiff.formats.get_formats import get_format
from gendiff.formats.formatter import unify_values
from gendiff.parse import parse


def generate_diff(first_file, second_file, format='stylish'):
    with open(first_file, 'r') as f1, open(second_file, 'r') as f2:
        file1 = f1.read()
        file2 = f2.read()
        result = builder_tree(parse(file1), parse(file2))
        return get_format(format, result)

    # read files
    # data1 = parse(first_file)
    # data2 = parse(second_file)
    #
    # tree = builderTree(data1, data2)
    # return formatter(tree)

    # diff = []
    # data1 = check_boolean(dict(sorted(data1.items())))
    # data2 = check_boolean(dict(sorted(data2.items())))
    # for key1 in data1:
    #     if key1 not in data2:
    #         diff.append(f'  - {key1}: {data1[key1]}')
    #     else:
    #         if data1[key1] == data2[key1]:
    #             diff.append(f'    {key1}: {data1[key1]}')
    #         else:
    #             diff.append(f'  - {key1}: {data1[key1]}')
    #             diff.append(f'  + {key1}: {data2[key1]}')
    # for key2 in data2:
    #     if key2 not in data1:
    #         diff.append(f'  + {key2}: {data2[key2]}')
    # diff = '\n'.join(diff)
    # return '{\n' + diff + '\n''}\n'

# def check_boolean(data):
#     for key in data.keys():
#         if data.get(key) is False:
#             data[key] = 'false'
#         if data.get(key) is True:
#             data[key] = 'true'
#     return data


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
