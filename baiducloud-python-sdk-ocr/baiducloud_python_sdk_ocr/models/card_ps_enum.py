"""
CardPsEnum information
"""


class CardPsEnum:
    """
    Enum class for CardPsEnum
    Allowed values: VALUE_MINUS_1, VALUE_0, VALUE_1
    """

    VALUE_MINUS_1 = -1
    VALUE_0 = 0
    VALUE_1 = 1

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [-1, 0, 1]
        return value in valid_values
