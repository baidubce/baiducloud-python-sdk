"""
Os information
"""


class Os:
    """
    Enum class for Os
    Allowed values: LINUX, WINDOWS
    """

    LINUX = 'LINUX'
    WINDOWS = 'WINDOWS'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['LINUX', 'WINDOWS']
        return value in valid_values
