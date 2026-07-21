"""
ExpansionStrategy information
"""


class ExpansionStrategy:
    """
    Enum class for ExpansionStrategy
    Allowed values: PRIORITY, BALANCED
    """

    PRIORITY = 'Priority'
    BALANCED = 'Balanced'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['Priority', 'Balanced']
        return value in valid_values
