"""
ImageStatus information
"""


class ImageStatus:
    """
    Enum class for ImageStatus
    Allowed values: CREATING, CREATEDFAILED, AVAILABLE, NOTAVAILABLE, ERROR
    """

    CREATING = 'Creating'
    CREATEDFAILED = 'CreatedFailed'
    AVAILABLE = 'Available'
    NOTAVAILABLE = 'NotAvailable'
    ERROR = 'Error'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['Creating', 'CreatedFailed', 'Available', 'NotAvailable', 'Error']
        return value in valid_values
