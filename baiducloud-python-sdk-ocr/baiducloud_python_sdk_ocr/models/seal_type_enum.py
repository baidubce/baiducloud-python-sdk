"""
SealTypeEnum information
"""


class SealTypeEnum:
    """
    Enum class for SealTypeEnum
    Allowed values: CIRCLE, ELLIPSE, RECTANGLE, PERFORATION
    """

    CIRCLE = 'circle'
    ELLIPSE = 'ellipse'
    RECTANGLE = 'rectangle'
    PERFORATION = 'perforation'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['circle', 'ellipse', 'rectangle', 'perforation']
        return value in valid_values
