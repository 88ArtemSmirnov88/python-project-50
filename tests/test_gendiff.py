import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, format, expected', [
    ('tests/fixtures/file.json',
     'tests/fixtures/file2.json',
     'stylish',
     'tests/fixtures/result_stylish.txt'),
    ('tests/fixtures/file.yaml',
     'tests/fixtures/file2.yaml',
     'stylish',
     'tests/fixtures/result_stylish.txt'),
    ('tests/fixtures/file.json',
     'tests/fixtures/file2.json',
     'plain',
     'tests/fixtures/result_plain.txt'),
    ('tests/fixtures/file.yaml',
     'tests/fixtures/file2.yaml',
     'plain',
     'tests/fixtures/result_plain.txt'),
    ('tests/fixtures/file.json',
     'tests/fixtures/file2.json',
     'json',
     'tests/fixtures/result_json.txt'),
    ('tests/fixtures/file.yaml',
     'tests/fixtures/file2.yaml',
     'json',
     'tests/fixtures/result_json.txt')
])
def test_gendiff(file1, file2, format, expected):
    with open(expected, 'r') as f1:
        result = f1.read()
        assert generate_diff(file1, file2, format) == result


# def test_gendiff_stylish_json():
#     test_json = generate_diff('tests/fixtures/file.json',
#                               'tests/fixtures/file2.json')
#     result = open('tests/fixtures/result_stylish.txt').read()
#     assert test_json == result
#
#
# def test_gendiff_stylish_yaml():
#     test_yaml = generate_diff('tests/fixtures/file.yaml',
#                               'tests/fixtures/file2.yaml')
#     result = open('tests/fixtures/result_stylish.txt').read()
#     assert test_yaml == result
#
#
# def test_gendiff_plain_json():
#     test_json = generate_diff('tests/fixtures/file.json',
#                               'tests/fixtures/file2.json', format='plain')
#     result = open('tests/fixtures/result_plain.txt').read()
#     assert test_json == result
#
#
# def test_gendiff_plain_yaml():
#     test_yaml = generate_diff('tests/fixtures/file.yaml',
#                               'tests/fixtures/file2.yaml', format='plain')
#     result = open('tests/fixtures/result_plain.txt').read()
#     assert test_yaml == result
#
#
# def test_gendiff_json_json():
#     test_json = generate_diff('tests/fixtures/file.json',
#                               'tests/fixtures/file2.json', format='json')
#     result = open('tests/fixtures/result_json.txt').read()
#     assert test_json == result
#
#
# def test_gendiff_json_json():
#     test_json = generate_diff('tests/fixtures/file.yaml',
#                               'tests/fixtures/file2.yaml', format='json')
#     result = open('tests/fixtures/result_json.txt').read()
#     assert test_json == result
