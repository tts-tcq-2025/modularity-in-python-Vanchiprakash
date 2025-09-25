from color_pair_utils import color_pair_from_number, pair_number_from_color_pair

def test_number_to_pair(pair_number, expected_major, expected_minor, *args, **kwargs):
    """
    Test conversion from pair number to color pair.
    Accepts extra arguments for future compatibility.
    """
    major, minor = color_pair_from_number(pair_number)
    assert major == expected_major, f"Expected major {expected_major}, got {major}"
    assert minor == expected_minor, f"Expected minor {expected_minor}, got {minor}"

def test_pair_to_number(major, minor, expected_number, *args, **kwargs):
    """
    Test conversion from color pair to pair number.
    Accepts extra arguments for future compatibility.
    """
    number = pair_number_from_color_pair(major, minor)
    assert number == expected_number, f"Expected number {expected_number}, got {number}"

def run_color_pair_tests():
    """
    Runs all color pair conversion tests.
    """
    test_cases_number_to_pair = [
        (4, 'White', 'Brown'),
        (5, 'White', 'Slate'),
    ]
    test_cases_pair_to_number = [
        ('Black', 'Orange', 12),
        ('Violet', 'Slate', 25),
        ('Red', 'Orange', 7),
    ]

    for case in test_cases_number_to_pair:
        test_number_to_pair(*case)

    for case in test_cases_pair_to_number:
        test_pair_to_number(*case)
