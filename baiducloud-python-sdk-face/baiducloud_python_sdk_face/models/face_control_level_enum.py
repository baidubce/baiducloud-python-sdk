"""
FaceControlLevelEnum information
"""


class FaceControlLevelEnum:
    """
    Enum class for FaceControlLevelEnum
    Allowed values: NONE, LOW, NORMAL, HIGH
    """

    NONE = 'NONE'
    LOW = 'LOW'
    NORMAL = 'NORMAL'
    HIGH = 'HIGH'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['NONE', 'LOW', 'NORMAL', 'HIGH']
        return value in valid_values
