from gendiff import generate_diff


def test_gendiff():
    test_json = generate_diff('tests/fixtures/file1.json',
                              'tests/fixtures/file2.json')
    test_yaml = generate_diff('tests/fixtures/file1.yaml',
                              'tests/fixtures/file2.yaml')
    result = open('tests/fixtures/result_json.txt').read()
    assert test_json == result
    assert test_yaml == result


def test_gendiff_stylish_json():
    test_json = generate_diff('tests/fixtures/file3.json',
                              'tests/fixtures/file4.json')
    result = open('tests/fixtures/result_stylish.txt').read()
    assert test_json == result


def test_gendiff_stylish_yaml():
    test_yaml = generate_diff('tests/fixtures/file3.yaml',
                              'tests/fixtures/file4.yaml')
    result = open('tests/fixtures/result_stylish.txt').read()
    assert test_yaml == result