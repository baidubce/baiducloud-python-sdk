"""
AccuracyEnum information
"""


class AccuracyEnum:
    """
    Enum class for AccuracyEnum
    Allowed values: NORMAL, HIGH
    """

    NORMAL = 'normal'
    HIGH = 'high'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['normal', 'high']
        return value in valid_values
