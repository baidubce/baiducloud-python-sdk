"""
LineClassEnum information
"""


class LineClassEnum:
    """
    Enum class for LineClassEnum
    Allowed values: KEY, VALUE, TABLE_VALUE, OTHER
    """

    KEY = 'key'
    VALUE = 'value'
    TABLE_VALUE = 'table_value'
    OTHER = 'other'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['key', 'value', 'table_value', 'other']
        return value in valid_values
