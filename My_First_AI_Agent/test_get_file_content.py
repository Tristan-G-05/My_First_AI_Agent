from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_lorem_truncation():
    content = get_file_content("calculator", "lorem.txt")

    assert len(content) > MAX_CHARS
    assert 'truncated at' in content
    assert content.endswith(f'... File "lorem.txt" truncated at {MAX_CHARS} characters.')

def test_main_py():
    print(get_file_content("calculator", "main.py"))

def test_pkg_calculator():
    print(get_file_content("calculator", "pkg/calculator.py"))

def test_outside_working_dir():
    print(get_file_content("calculator", "/bin/cat"))

def test_missing_file():
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

def test():
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    test()