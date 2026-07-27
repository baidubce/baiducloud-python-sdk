"""
InstanceType information
"""


class InstanceType:
    """
    Enum class for InstanceType
    Allowed values: BCC, BBC, HPAS
    """

    BCC = 'BCC'
    BBC = 'BBC'
    HPAS = 'HPAS'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['BCC', 'BBC', 'HPAS']
        return value in valid_values
