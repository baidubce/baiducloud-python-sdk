"""
SwitchDigitalWidthEnum information
"""


class SwitchDigitalWidthEnum:
    """
    Enum class for SwitchDigitalWidthEnum
    Allowed values: AUTO, HALF, FULL
    """

    AUTO = 'auto'
    HALF = 'half'
    FULL = 'full'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['auto', 'half', 'full']
        return value in valid_values
