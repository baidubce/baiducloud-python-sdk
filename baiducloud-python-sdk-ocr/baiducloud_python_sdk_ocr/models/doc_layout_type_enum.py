"""
DocLayoutTypeEnum information
"""


class DocLayoutTypeEnum:
    """
    Enum class for DocLayoutTypeEnum
    Allowed values: TABLE, FIGURE, TEXT, TITLE, CONTENTS, SEAL, TABLE_TITLE, FIGURE_TITLE, DOC_TITLE
    """

    TABLE = 'table'
    FIGURE = 'figure'
    TEXT = 'text'
    TITLE = 'title'
    CONTENTS = 'contents'
    SEAL = 'seal'
    TABLE_TITLE = 'table_title'
    FIGURE_TITLE = 'figure_title'
    DOC_TITLE = 'doc_title'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'table',
            'figure',
            'text',
            'title',
            'contents',
            'seal',
            'table_title',
            'figure_title',
            'doc_title',
        ]
        return value in valid_values
