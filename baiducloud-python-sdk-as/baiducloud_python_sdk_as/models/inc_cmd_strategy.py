"""
IncCmdStrategy information
"""


class IncCmdStrategy:
    """
    Enum class for IncCmdStrategy
    Allowed values: PROCEED, PAUSE
    """

    PROCEED = 'Proceed'
    PAUSE = 'Pause'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['Proceed', 'Pause']
        return value in valid_values
