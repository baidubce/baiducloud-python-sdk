"""
AgentState information
"""


class AgentState:
    """
    Enum class for AgentState
    Allowed values: ONLINE, OFFLINE
    """

    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['ONLINE', 'OFFLINE']
        return value in valid_values
