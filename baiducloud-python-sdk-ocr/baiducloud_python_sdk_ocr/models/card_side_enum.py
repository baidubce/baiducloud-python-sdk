"""
CardSideEnum information
"""


class CardSideEnum:
    """
    Enum class for CardSideEnum
    Allowed values: IDCARD_FRONT, IDCARD_BACK
    """

    IDCARD_FRONT = 'idcard_front'
    IDCARD_BACK = 'idcard_back'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['idcard_front', 'idcard_back']
        return value in valid_values
