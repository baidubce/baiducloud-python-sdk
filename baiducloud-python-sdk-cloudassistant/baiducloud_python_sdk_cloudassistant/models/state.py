"""
State information
"""


class State:
    """
    Enum class for State
    Allowed values: FAILED, RUNNING, SUCCESS, PARTIAL_FAILED, PENDING
    """

    FAILED = 'FAILED'
    RUNNING = 'RUNNING'
    SUCCESS = 'SUCCESS'
    PARTIAL_FAILED = 'PARTIAL_FAILED'
    PENDING = 'PENDING'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['FAILED', 'RUNNING', 'SUCCESS', 'PARTIAL_FAILED', 'PENDING']
        return value in valid_values
