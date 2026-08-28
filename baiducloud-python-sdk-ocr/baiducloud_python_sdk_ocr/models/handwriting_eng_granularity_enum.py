"""
HandwritingEngGranularityEnum information
"""


class HandwritingEngGranularityEnum:
    """
    Enum class for HandwritingEngGranularityEnum
    Allowed values: LETTER, WORD
    """

    LETTER = 'letter'
    WORD = 'word'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['letter', 'word']
        return value in valid_values
