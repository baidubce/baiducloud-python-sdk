"""
SegmentReturnFormEnum information
"""


class SegmentReturnFormEnum:
    """
    Enum class for SegmentReturnFormEnum
    Allowed values: RGBA, MASK
    """

    RGBA = 'rgba'
    MASK = 'mask'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['rgba', 'mask']
        return value in valid_values
