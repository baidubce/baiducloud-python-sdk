"""
ActionType information
"""


class ActionType:
    """
    Enum class for ActionType
    Allowed values: INCREASE, DECREASE, ADJUST
    """

    INCREASE = 'INCREASE'
    DECREASE = 'DECREASE'
    ADJUST = 'ADJUST'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['INCREASE', 'DECREASE', 'ADJUST']
        return value in valid_values
