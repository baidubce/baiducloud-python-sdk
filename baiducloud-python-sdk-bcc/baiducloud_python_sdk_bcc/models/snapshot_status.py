"""
SnapshotStatus information
"""


class SnapshotStatus:
    """
    Enum class for SnapshotStatus
    Allowed values: CREATING, CREATEDFAILED, AVAILABLE, NOTAVAILABLE
    """

    CREATING = 'Creating'
    CREATEDFAILED = 'CreatedFailed'
    AVAILABLE = 'Available'
    NOTAVAILABLE = 'NotAvailable'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['Creating', 'CreatedFailed', 'Available', 'NotAvailable']
        return value in valid_values
