"""
FaceUpdateActionEnum information
"""


class FaceUpdateActionEnum:
    """
    Enum class for FaceUpdateActionEnum
    Allowed values: UPDATE, REPLACE
    """

    UPDATE = 'UPDATE'
    REPLACE = 'REPLACE'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['UPDATE', 'REPLACE']
        return value in valid_values
