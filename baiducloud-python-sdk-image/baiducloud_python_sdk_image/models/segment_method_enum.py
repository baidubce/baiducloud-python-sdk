"""
SegmentMethodEnum information
"""


class SegmentMethodEnum:
    """
    Enum class for SegmentMethodEnum
    Allowed values: AUTO, CONTROL
    """

    AUTO = 'auto'
    CONTROL = 'control'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['auto', 'control']
        return value in valid_values
