import re


def test_valid_regex(pattern):
    """
    Tests whether or not the input string is a valid regular expression.

    Args:
        pattern: String representing the regular expression to test for validity.
    Returns:
        bool: Is the pattern a valid regular expression?
    """
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


if __name__ == '__main__':
    for i in range(int(input())):
        print(test_valid_regex(input()))
