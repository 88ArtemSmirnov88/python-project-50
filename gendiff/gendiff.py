import json


def parse(file):
    with open(file, 'r') as data:
        return json.load(data)


def generate_diff(first_file, second_file):
    data1 = parse(first_file)
    data2 = parse(second_file)
    diff = []
    data1 = check_boolean(dict(sorted(data1.items())))
    data2 = check_boolean(dict(sorted(data2.items())))
    for key1 in data1:
        if key1 not in data2:
            diff.append(f' - {key1}: {data1[key1]}')
        else:
            if data1[key1] == data2[key1]:
                diff.append(f'   {key1}: {data1[key1]}')
            else:
                diff.append(f' - {key1}: {data1[key1]}')
                diff.append(f' + {key1}: {data2[key1]}')
    for key2 in data2:
        if key2 not in data1:
            diff.append(f' + {key2}: {data2[key2]}')
    diff = '\n'.join(diff)
    return '{\n' + diff + '\n''}'


def check_boolean(data):
    for key in data.keys():
        if data.get(key) is False:
            data[key] = 'false'
        if data.get(key) is True:
            data[key] = 'true'
    return data
