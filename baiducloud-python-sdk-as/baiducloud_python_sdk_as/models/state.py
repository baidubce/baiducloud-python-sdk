"""
State information
"""


class State:
    """
    Enum class for State
    Allowed values: ENABLE, DISABLE
    """

    ENABLE = 'ENABLE'
    DISABLE = 'DISABLE'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['ENABLE', 'DISABLE']
        return value in valid_values
