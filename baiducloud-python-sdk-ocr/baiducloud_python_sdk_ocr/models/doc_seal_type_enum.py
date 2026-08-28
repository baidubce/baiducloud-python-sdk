"""
DocSealTypeEnum information
"""


class DocSealTypeEnum:
    """
    Enum class for DocSealTypeEnum
    Allowed values: CIRCLE, ELLIPSE, RECTANGLE
    """

    CIRCLE = 'circle'
    ELLIPSE = 'ellipse'
    RECTANGLE = 'rectangle'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['circle', 'ellipse', 'rectangle']
        return value in valid_values
