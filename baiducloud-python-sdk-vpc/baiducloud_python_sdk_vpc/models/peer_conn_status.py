"""
PeerConnStatus information
"""


class PeerConnStatus:
    """
    Enum class for PeerConnStatus
    """

    CREATING = 'creating'
    CONSULTING = 'consulting'
    CONSULT_FAILED = 'consult_failed'
    ACTIVE = 'active'
    DOWN = 'down'
    STARTING = 'starting'
    STOPPING = 'stopping'
    DELETING = 'deleting'
    DELETED = 'deleted'
    EXPIRED = 'expired'
    ERROR = 'error'
    UPDATING = 'updating'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'creating',
            'consulting',
            'consult_failed',
            'active',
            'down',
            'starting',
            'stopping',
            'deleting',
            'deleted',
            'expired',
            'error',
            'updating',
        ]
        return value in valid_values
