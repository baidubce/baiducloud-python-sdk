"""
SceneTypeEnum information
"""


class SceneTypeEnum:
    """
    Enum class for SceneTypeEnum
    Allowed values: PAPER, ANSWER_SHEET
    """

    PAPER = 'paper'
    ANSWER_SHEET = 'answer_sheet'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['paper', 'answer_sheet']
        return value in valid_values
