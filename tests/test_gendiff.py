import pytest
from gendiff import generate_diff


def get_path(file_name):
    return f'tests/fixtures/{file_name}'


def read_file(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize('format', ['json', 'yaml'])
def test_gendiff(format):
    file_path1 = get_path(f'file.{format}')
    file_path2 = get_path(f'file2.{format}')

    assert generate_diff(file_path1, file_path2, 'stylish') == read_file(get_path('result_stylish.txt'))
    assert generate_diff(file_path1, file_path2, 'plain') == read_file(get_path('result_plain.txt'))
    assert generate_diff(file_path1, file_path2, 'json') == read_file(get_path('result_json.txt'))

