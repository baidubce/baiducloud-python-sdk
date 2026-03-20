"""
EipStatus information
"""


class EipStatus:
    """
    Enum class for EipStatus
    Allowed values: CREATING, AVAILABLE, BINDED, BINDING, UNBINDING, UPDATING, PAUSED, UNAVAILABLE
    """

    CREATING = 'creating'
    AVAILABLE = 'available'
    BINDED = 'binded'
    BINDING = 'binding'
    UNBINDING = 'unbinding'
    UPDATING = 'updating'
    PAUSED = 'paused'
    UNAVAILABLE = 'unavailable'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['creating', 'available', 'binded', 'binding', 'unbinding', 'updating', 'paused', 'unavailable']
        return value in valid_values
