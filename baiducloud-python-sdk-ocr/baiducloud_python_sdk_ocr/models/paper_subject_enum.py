"""
PaperSubjectEnum information
"""


class PaperSubjectEnum:
    """
    Enum class for PaperSubjectEnum
    Allowed values: CHINESE, MATH, ENGLISH, PHYSICS, CHEMISTRY, BIOLOGY, HISTORY, GEOGRAPHY, POLITICS
    """

    CHINESE = 'chinese'
    MATH = 'math'
    ENGLISH = 'english'
    PHYSICS = 'physics'
    CHEMISTRY = 'chemistry'
    BIOLOGY = 'biology'
    HISTORY = 'history'
    GEOGRAPHY = 'geography'
    POLITICS = 'politics'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'chinese',
            'math',
            'english',
            'physics',
            'chemistry',
            'biology',
            'history',
            'geography',
            'politics',
        ]
        return value in valid_values
