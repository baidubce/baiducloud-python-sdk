"""
BlbStatus information
"""


class BlbStatus:
    """
    Enum class for BlbStatus
    Allowed values: CREATING, AVAILABLE, UPDATING, PAUSED, UNAVAILABLE
    """

    CREATING = 'creating'
    AVAILABLE = 'available'
    UPDATING = 'updating'
    PAUSED = 'paused'
    UNAVAILABLE = 'unavailable'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['creating', 'available', 'updating', 'paused', 'unavailable']
        return value in valid_values
