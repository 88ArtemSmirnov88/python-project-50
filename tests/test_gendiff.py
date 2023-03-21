from gendiff import generate_diff


def test_gendiff_stylish_json():
    test_json = generate_diff('tests/fixtures/file.json',
                              'tests/fixtures/file2.json')
    result = open('tests/fixtures/result_stylish.txt').read()
    assert test_json == result


def test_gendiff_stylish_yaml():
    test_yaml = generate_diff('tests/fixtures/file.yaml',
                              'tests/fixtures/file2.yaml')
    result = open('tests/fixtures/result_stylish.txt').read()
    assert test_yaml == result


def test_gendiff_plain_json():
    test_json = generate_diff('tests/fixtures/file.json',
                              'tests/fixtures/file2.json', format='plain')
    result = open('tests/fixtures/result_plain.txt').read()
    assert test_json == result


def test_gendiff_plain_yaml():
    test_yaml = generate_diff('tests/fixtures/file.yaml',
                              'tests/fixtures/file2.yaml', format='plain')
    result = open('tests/fixtures/result_plain.txt').read()
    assert test_yaml == result


def test_gendiff_json_json():
    test_json = generate_diff('tests/fixtures/file.json',
                              'tests/fixtures/file2.json', format='json')
    result = open('tests/fixtures/result_json.txt').read()
    assert test_json == result


def test_gendiff_json_json():
    test_json = generate_diff('tests/fixtures/file.yaml',
                              'tests/fixtures/file2.yaml', format='json')
    result = open('tests/fixtures/result_json.txt').read()
    assert test_json == result
