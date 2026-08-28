"""
PaperCutLanguageTypeEnum information
"""


class PaperCutLanguageTypeEnum:
    """
    Enum class for PaperCutLanguageTypeEnum
    Allowed values: CHN_ENG, ENG
    """

    CHN_ENG = 'CHN_ENG'
    ENG = 'ENG'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['CHN_ENG', 'ENG']
        return value in valid_values
