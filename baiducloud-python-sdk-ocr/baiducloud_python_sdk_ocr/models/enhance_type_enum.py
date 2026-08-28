"""
EnhanceTypeEnum information
"""


class EnhanceTypeEnum:
    """
    Enum class for EnhanceTypeEnum
    Allowed values: VALUE_0, VALUE_1, VALUE_2, VALUE_3
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [0, 1, 2, 3]
        return value in valid_values
