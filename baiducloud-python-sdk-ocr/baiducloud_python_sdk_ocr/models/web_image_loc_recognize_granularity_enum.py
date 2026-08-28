"""
WebImageLocRecognizeGranularityEnum information
"""


class WebImageLocRecognizeGranularityEnum:
    """
    Enum class for WebImageLocRecognizeGranularityEnum
    Allowed values: BIG, SMALL
    """

    BIG = 'big'
    SMALL = 'small'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['big', 'small']
        return value in valid_values
