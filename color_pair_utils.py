from color_constants import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
    """
    Return a string representation of a color pair.
    :return: String in the format 'Major Minor'.
    """
    return f'{major_color} {minor_color}'

def color_pair_from_number(pair_number):
    """
    Given a pair number, return the corresponding major and minor colors.
    :param pair_number: The cable pair number (1-based).
    :return: Tuple (major_color, minor_color).
    :raises Exception: If the major index is out of range.
    """
    # Convert to zero-based index for calculation
    zero_based_pair_number = pair_number - 1
    # Calculate major color index
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    # Calculate minor color index
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def pair_number_from_color_pair(major_color, minor_color):
    """
    Given major and minor colors, return the corresponding pair number.
    :return: The cable pair number (1-based).
    :raises Exception: If colors are not found in the lists.
    """
    # Find index of major color
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    # Find index of minor color
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    # Calculate pair number from indices
    return major_index * len(MINOR_COLORS) + minor_index + 1
