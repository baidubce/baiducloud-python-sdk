"""
ShrinkageStrategy information
"""


class ShrinkageStrategy:
    """
    Enum class for ShrinkageStrategy
    Allowed values: EARLIER, LATER
    """

    EARLIER = 'Earlier'
    LATER = 'Later'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['Earlier', 'Later']
        return value in valid_values
