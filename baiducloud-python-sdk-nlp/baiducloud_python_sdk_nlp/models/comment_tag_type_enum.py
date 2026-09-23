"""
CommentTagTypeEnum information
"""


class CommentTagTypeEnum:
    """
    Enum class for CommentTagTypeEnum
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        return value in valid_values
