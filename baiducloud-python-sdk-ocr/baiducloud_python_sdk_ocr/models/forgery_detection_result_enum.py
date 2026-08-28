"""
ForgeryDetectionResultEnum information
"""


class ForgeryDetectionResultEnum:
    """
    Enum class for ForgeryDetectionResultEnum
    Allowed values: FAKE, REAL
    """

    FAKE = 'fake'
    REAL = 'real'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['fake', 'real']
        return value in valid_values
