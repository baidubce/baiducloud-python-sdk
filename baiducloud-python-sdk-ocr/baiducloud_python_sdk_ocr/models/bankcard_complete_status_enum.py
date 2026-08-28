"""
BankcardCompleteStatusEnum information
"""


class BankcardCompleteStatusEnum:
    """
    Enum class for BankcardCompleteStatusEnum
    Allowed values: VALUE_0, VALUE_1
    """

    VALUE_0 = 0
    VALUE_1 = 1

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [0, 1]
        return value in valid_values
