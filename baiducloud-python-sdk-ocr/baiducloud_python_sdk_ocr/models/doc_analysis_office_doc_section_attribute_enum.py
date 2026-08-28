"""
DocAnalysisOfficeDocSectionAttributeEnum information
"""


class DocAnalysisOfficeDocSectionAttributeEnum:
    """
    Enum class for DocAnalysisOfficeDocSectionAttributeEnum
    Allowed values: SECTION, HEADER, FOOTER, NUMBER, FOOTNOTE
    """

    SECTION = 'section'
    HEADER = 'header'
    FOOTER = 'footer'
    NUMBER = 'number'
    FOOTNOTE = 'footnote'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['section', 'header', 'footer', 'number', 'footnote']
        return value in valid_values
