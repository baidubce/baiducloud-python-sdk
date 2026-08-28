"""
QuestionElementTypeEnum information
"""


class QuestionElementTypeEnum:
    """
    Enum class for QuestionElementTypeEnum
    Allowed values: VALUE_0, VALUE_1, VALUE_2, VALUE_3, VALUE_4, VALUE_5
    """

    VALUE_0 = '0'
    VALUE_1 = '1'
    VALUE_2 = '2'
    VALUE_3 = '3'
    VALUE_4 = '4'
    VALUE_5 = '5'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['0', '1', '2', '3', '4', '5']
        return value in valid_values
