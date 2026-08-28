"""
PassportDirectionEnum information
"""


class PassportDirectionEnum:
    """
    Enum class for PassportDirectionEnum
    Allowed values: VALUE_MINUS_1, VALUE_0, VALUE_1, VALUE_2, VALUE_3
    """

    VALUE_MINUS_1 = -1
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [-1, 0, 1, 2, 3]
        return value in valid_values
