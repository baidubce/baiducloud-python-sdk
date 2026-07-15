"""
State information
"""


class State:
    """
    Enum class for State
    Allowed values: FAILED, RUNNING, SUCCESS
    """

    FAILED = 'FAILED'
    RUNNING = 'RUNNING'
    SUCCESS = 'SUCCESS'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['FAILED', 'RUNNING', 'SUCCESS']
        return value in valid_values
