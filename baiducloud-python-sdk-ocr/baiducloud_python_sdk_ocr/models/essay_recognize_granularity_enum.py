"""
EssayRecognizeGranularityEnum information
"""


class EssayRecognizeGranularityEnum:
    """
    Enum class for EssayRecognizeGranularityEnum
    Allowed values: LINE, WORD, NONE
    """

    LINE = 'line'
    WORD = 'word'
    NONE = 'none'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['line', 'word', 'none']
        return value in valid_values
