"""
InstanceType information
"""


class InstanceType:
    """
    Enum class for InstanceType
    Allowed values: BCC, BBC
    """

    BCC = 'BCC'
    BBC = 'BBC'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['BCC', 'BBC']
        return value in valid_values
