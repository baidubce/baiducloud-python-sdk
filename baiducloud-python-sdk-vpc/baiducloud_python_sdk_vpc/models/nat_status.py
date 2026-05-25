"""
NatStatus information
"""


class NatStatus:
    """
    Enum class for NatStatus
    """

    ACTIVE = 'active'
    UPDATING = 'updating'
    UNCONFIGURED = 'unconfigured'
    DOWN = 'down'
    BUILDING = 'building'
    ERROR = 'error'
    DELETING = 'deleting'
    DELETED = 'deleted'
    STARTING = 'starting'
    CONFIGURING = 'configuring'
    REBOOTING = 'rebooting'
    STOPPING = 'stopping'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'active',
            'updating',
            'unconfigured',
            'down',
            'building',
            'error',
            'deleting',
            'deleted',
            'starting',
            'configuring',
            'rebooting',
            'stopping',
        ]
        return value in valid_values
