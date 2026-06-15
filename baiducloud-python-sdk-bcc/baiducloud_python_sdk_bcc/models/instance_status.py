"""
InstanceStatus information
"""


class InstanceStatus:
    """
    Enum class for InstanceStatus
    """

    STARTING = 'Starting'
    RUNNING = 'Running'
    STOPPING = 'Stopping'
    STOPPED = 'Stopped'
    RECYCLED = 'Recycled'
    DELETED = 'Deleted'
    SCALING = 'Scaling'
    EXPIRED = 'Expired'
    ERROR = 'Error'
    SNAPSHOTPROCESSING = 'SnapshotProcessing'
    IMAGEPROCESSING = 'ImageProcessing'
    RECHARGING = 'Recharging'
    VOLUMERESIZING = 'VolumeResizing'
    BILLINGCHANGING = 'BillingChanging'
    CHANGESUBNET = 'ChangeSubnet'
    CHANGEVPC = 'ChangeVpc'
    ATTACHINGPORT = 'AttachingPort'
    DETACHINGPORT = 'DetachingPort'
    MOVING = 'Moving'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'Starting',
            'Running',
            'Stopping',
            'Stopped',
            'Recycled',
            'Deleted',
            'Scaling',
            'Expired',
            'Error',
            'SnapshotProcessing',
            'ImageProcessing',
            'Recharging',
            'VolumeResizing',
            'BillingChanging',
            'ChangeSubnet',
            'ChangeVpc',
            'AttachingPort',
            'DetachingPort',
            'Moving',
        ]
        return value in valid_values
