"""
LicensePlateColorEnum information
"""


class LicensePlateColorEnum:
    """
    Enum class for LicensePlateColorEnum
    Allowed values: BLUE, GREEN, YELLOW, WHITE, BLACK, YELLOW_GREEN, UNKNOW, PENYIN
    """

    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    WHITE = 'white'
    BLACK = 'black'
    YELLOW_GREEN = 'yellow_green'
    UNKNOW = 'unknow'
    PENYIN = 'penyin'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['blue', 'green', 'yellow', 'white', 'black', 'yellow_green', 'unknow', 'penyin']
        return value in valid_values
