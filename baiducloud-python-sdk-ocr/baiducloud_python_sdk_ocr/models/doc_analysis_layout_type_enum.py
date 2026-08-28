"""
DocAnalysisLayoutTypeEnum information
"""


class DocAnalysisLayoutTypeEnum:
    """
    Enum class for DocAnalysisLayoutTypeEnum
    Allowed values: TABLE, FIGURE, TEXT, TITLE, CONTENTS
    """

    TABLE = 'table'
    FIGURE = 'figure'
    TEXT = 'text'
    TITLE = 'title'
    CONTENTS = 'contents'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['table', 'figure', 'text', 'title', 'contents']
        return value in valid_values
