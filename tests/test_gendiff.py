from gendiff import generate_diff


def test_gendiff():
    test_json = generate_diff('tests/fixtures/file1.json',
                              'tests/fixtures/file2.json')
    test_yaml = generate_diff('tests/fixtures/file1.yaml',
                              'tests/fixtures/file2.yaml')
    result = open('tests/fixtures/result_json.txt').read()
    assert test_json == result
    assert test_yaml == result
