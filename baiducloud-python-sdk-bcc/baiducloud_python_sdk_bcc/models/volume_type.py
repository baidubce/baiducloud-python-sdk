"""
VolumeType information
"""


class VolumeType:
    """
    Enum class for VolumeType
    Allowed values: SYSTEM, EPHEMERAL, CDS
    """

    SYSTEM = 'System'
    EPHEMERAL = 'Ephemeral'
    CDS = 'Cds'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['System', 'Ephemeral', 'Cds']
        return value in valid_values
