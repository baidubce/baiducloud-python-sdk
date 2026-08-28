"""
WordsAttributeEnum information
"""


class WordsAttributeEnum:
    """
    Enum class for WordsAttributeEnum
    Allowed values: HANDWRITING, PRINT
    """

    HANDWRITING = 'handwriting'
    PRINT = 'print'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['handwriting', 'print']
        return value in valid_values
