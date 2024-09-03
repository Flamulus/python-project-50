from gendiff import generate_diff


def test_generate_diff():
    # assert generate_diff() == diff_flat_files
    result = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    )
    with_links_path = 'tests/fixtures/diff_flat_files.txt'
    with open(with_links_path, encoding='utf8') as f:
        txt = f.read()
        assert "".join(txt) == result
    
