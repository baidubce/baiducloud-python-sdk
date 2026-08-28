"""
EducationPaperCutEduWordsTypeEnum information
"""


class EducationPaperCutEduWordsTypeEnum:
    """
    Enum class for EducationPaperCutEduWordsTypeEnum
    Allowed values: HANDWRING_ONLY, HANDPRINT_MIX
    """

    HANDWRING_ONLY = 'handwring_only'
    HANDPRINT_MIX = 'handprint_mix'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['handwring_only', 'handprint_mix']
        return value in valid_values
