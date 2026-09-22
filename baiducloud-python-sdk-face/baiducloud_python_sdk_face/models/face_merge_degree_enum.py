"""
FaceMergeDegreeEnum information
"""


class FaceMergeDegreeEnum:
    """
    Enum class for FaceMergeDegreeEnum
    Allowed values: LOW, NORMAL, HIGH, COMPLETE
    """

    LOW = 'LOW'
    NORMAL = 'NORMAL'
    HIGH = 'HIGH'
    COMPLETE = 'COMPLETE'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['LOW', 'NORMAL', 'HIGH', 'COMPLETE']
        return value in valid_values
