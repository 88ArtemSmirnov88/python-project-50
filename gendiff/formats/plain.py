def plain(tree, path):
    result = []
    for i in tree:
        value = i.get('value')
        value2 = i.get('value2')
        type = i.get('type')
        name = i.get('key')
        path.append(name)
        if type == 'added':
            result.append(
                "Property '{0}' was added with value: {1}".format(
                    '.'.join(path), format_value(value)))
        if type == 'deleted':
            result.append("Property '{0}' was removed".format('.'.join(path)))
        if type == 'changed':
            result.append("Property '{0}' was updated. From {1} to {2}".format(
                '.'.join(path), format_value(value),
                format_value(value2)))
        if type == 'nested':
            result.append(plain(value, path))
        path.pop()
    return '\n'.join(result)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is False:
        return 'false'
    elif value is True:
        return 'true'
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    else:
        return "'{0}'".format(value)


def get_plain_format(tree):
    return plain(tree, [])
