"""
Status information
"""


class Status:
    """
    Enum class for Status
    """

    CREATING = 'CREATING'
    RUNNING = 'RUNNING'
    SCALING_UP = 'SCALING_UP'
    SCALING_DOWN = 'SCALING_DOWN'
    ATTACHING_NODE = 'ATTACHING_NODE'
    DETACHING_NODE = 'DETACHING_NODE'
    DELETING = 'DELETING'
    BINDING_BLB = 'BINDING_BLB'
    UNBINDING_BLB = 'UNBINDING_BLB'
    COOLDOWN = 'COOLDOWN'
    PAUSE = 'PAUSE'
    DELETED = 'DELETED'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'CREATING',
            'RUNNING',
            'SCALING_UP',
            'SCALING_DOWN',
            'ATTACHING_NODE',
            'DETACHING_NODE',
            'DELETING',
            'BINDING_BLB',
            'UNBINDING_BLB',
            'COOLDOWN',
            'PAUSE',
            'DELETED',
        ]
        return value in valid_values
