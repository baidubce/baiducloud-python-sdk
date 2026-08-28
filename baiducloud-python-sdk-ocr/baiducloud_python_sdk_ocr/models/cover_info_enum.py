"""
CoverInfoEnum information
"""


class CoverInfoEnum:
    """
    Enum class for CoverInfoEnum
    Allowed values: INCOMPLETE, COMPLETE
    """

    INCOMPLETE = 'incomplete'
    COMPLETE = 'complete'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['incomplete', 'complete']
        return value in valid_values
