from gendiff import generate_diff


def test_gendiff():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'

    diff = generate_diff(path1, path2)
    result = open('tests/fixtures/result_json.txt').read()
    assert diff == result
