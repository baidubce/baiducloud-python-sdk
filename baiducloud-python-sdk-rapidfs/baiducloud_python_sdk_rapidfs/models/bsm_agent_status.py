"""
BsmAgentStatus information
"""


class BsmAgentStatus:
    """
    Enum class for BsmAgentStatus
    Allowed values: ONLINE, OFFLINE
    """

    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['ONLINE', 'OFFLINE']
        return value in valid_values
