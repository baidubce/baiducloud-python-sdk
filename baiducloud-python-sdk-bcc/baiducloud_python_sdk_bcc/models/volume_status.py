"""
VolumeStatus information
"""


class VolumeStatus:
    """
    Enum class for VolumeStatus
    """

    CREATING = 'Creating'
    AVAILABLE = 'Available'
    ATTACHING = 'Attaching'
    NOTAVAILABLE = 'NotAvailable'
    INUSE = 'InUse'
    DETACHING = 'Detaching'
    DELETING = 'Deleting'
    DELETED = 'Deleted'
    SCALING = 'Scaling'
    EXPIRED = 'Expired'
    ERROR = 'Error'
    SNAPSHOTPROCESSING = 'SnapshotProcessing'
    IMAGEPROCESSING = 'ImageProcessing'
    RECHARGING = 'Recharging'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'Creating',
            'Available',
            'Attaching',
            'NotAvailable',
            'InUse',
            'Detaching',
            'Deleting',
            'Deleted',
            'Scaling',
            'Expired',
            'Error',
            'SnapshotProcessing',
            'ImageProcessing',
            'Recharging',
        ]
        return value in valid_values
