"""
IdCardSideEnum information
"""


class IdCardSideEnum:
    """
    Enum class for IdCardSideEnum
    Allowed values: FRONT, BACK
    """

    FRONT = 'front'
    BACK = 'back'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['front', 'back']
        return value in valid_values
