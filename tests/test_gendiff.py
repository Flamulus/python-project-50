from gendiff import generate_diff


def test_generate_diff_flat_files():
    result_json = generate_diff(
        'tests/fixtures/flat_file1.json',
        'tests/fixtures/flat_file2.json'
    )
    result_yaml = generate_diff(
        'tests/fixtures/flat_file1.yaml',
        'tests/fixtures/flat_file2.yaml'
    )
    with_links_path = 'tests/fixtures/diff_flat_files.txt'

    with open(with_links_path, encoding='utf8') as f:
        txt = "".join(f.read())
        assert txt == result_json
        assert txt == result_yaml
