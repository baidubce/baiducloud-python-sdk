"""
DnsStatus information
"""


class DnsStatus:
    """
    Enum class for DnsStatus
    Allowed values: CLOSE, WAIT, SYNCING, OPEN, CLOSING
    """

    CLOSE = 'close'
    WAIT = 'wait'
    SYNCING = 'syncing'
    OPEN = 'open'
    CLOSING = 'closing'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['close', 'wait', 'syncing', 'open', 'closing']
        return value in valid_values
