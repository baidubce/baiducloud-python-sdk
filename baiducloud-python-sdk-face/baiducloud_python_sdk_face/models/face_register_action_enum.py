"""
FaceRegisterActionEnum information
"""


class FaceRegisterActionEnum:
    """
    Enum class for FaceRegisterActionEnum
    Allowed values: APPEND, REPLACE
    """

    APPEND = 'APPEND'
    REPLACE = 'REPLACE'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['APPEND', 'REPLACE']
        return value in valid_values
