"""
FourFactorsVerifyResultEnum information
"""


class FourFactorsVerifyResultEnum:
    """
    Enum class for FourFactorsVerifyResultEnum
    Allowed values: VALUE_1, VALUE_0, VALUE_2
    """

    VALUE_1 = '1'
    VALUE_0 = '0'
    VALUE_2 = '2'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['1', '0', '2']
        return value in valid_values
