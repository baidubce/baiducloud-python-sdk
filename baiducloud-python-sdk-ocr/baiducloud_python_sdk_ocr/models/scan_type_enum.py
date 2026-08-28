"""
ScanTypeEnum information
"""


class ScanTypeEnum:
    """
    Enum class for ScanTypeEnum
    Allowed values: VALUE_1, VALUE_2, VALUE_3
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [1, 2, 3]
        return value in valid_values
