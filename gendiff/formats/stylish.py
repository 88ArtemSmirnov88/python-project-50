EXTENDED_SPACE = ' '
COUNT_INDENT = 4


def stylish(tree, depth):
    result = ['{']
    open_indent = EXTENDED_SPACE * (COUNT_INDENT * depth - 2)
    close_indent = EXTENDED_SPACE * (COUNT_INDENT * (depth - 1))
    for node in tree:
        key = node.get('key')
        value = format_value(node.get('value'), depth + 1)
        type = node.get('type')
        if type == 'added':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='+', key=key,
                value=value
            ))
        elif type == 'deleted':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='-', key=key,
                value=value
            ))
        elif type == 'unchanged':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol=' ', key=key,
                value=value
            ))
        elif type == 'nested':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol=' ', key=key,
                value=stylish(node.get('value'), depth + 1)
            ))
        else:
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='-', key=key,
                value=value
            ))
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='+', key=key,
                value=format_value(node.get('value2'), depth + 1)
            ))
    result.append('{current_indent}{symbol}'.format(
        current_indent=close_indent, symbol='}'
    ))
    return '\n'.join(result)


def format_value(node, depth):
    open_indent = EXTENDED_SPACE * (COUNT_INDENT * depth - 2)
    close_indent = EXTENDED_SPACE * (COUNT_INDENT * (depth - 1))
    if isinstance(node, dict):
        result = ["{"]
        for key, value in node.items():
            # print('TEST[#1]: ', value)
            value = unify_values(value)
            # print('TEST[#2]: ', value)
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=open_indent, symbol=' ', key=key,
                value=format_value(value, depth + 1)
            ))
        result.append('{EXTENDED_SPACE}{symbol}'.format(
            EXTENDED_SPACE=close_indent, symbol='}'
        ))
        return '\n'.join(result)
    else:
        return unify_values(node)


def unify_values(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def get_stylish_format(tree):
    return stylish(tree, 1)
