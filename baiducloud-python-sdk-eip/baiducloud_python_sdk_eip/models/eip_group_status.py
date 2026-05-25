"""
EipGroupStatus information
"""


class EipGroupStatus:
    """
    Enum class for EipGroupStatus
    Allowed values: AVAILABLE, PAUSED, EXPIRED, DELETING
    """

    AVAILABLE = 'available'
    PAUSED = 'paused'
    EXPIRED = 'expired'
    DELETING = 'deleting'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['available', 'paused', 'expired', 'deleting']
        return value in valid_values
