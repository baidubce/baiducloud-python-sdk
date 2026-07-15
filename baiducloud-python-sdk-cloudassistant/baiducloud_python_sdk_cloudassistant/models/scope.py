"""
Scope information
"""


class Scope:
    """
    Enum class for Scope
    Allowed values: INDIVIDUAL, GLOBAL
    """

    INDIVIDUAL = 'INDIVIDUAL'
    GLOBAL = 'GLOBAL'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['INDIVIDUAL', 'GLOBAL']
        return value in valid_values
