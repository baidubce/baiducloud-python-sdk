"""
VehicleLicenseRiskTypeEnum information
"""


class VehicleLicenseRiskTypeEnum:
    """
    Enum class for VehicleLicenseRiskTypeEnum
    Allowed values: NORMAL, COPY, SCREEN
    """

    NORMAL = 'normal'
    COPY = 'copy'
    SCREEN = 'screen'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['normal', 'copy', 'screen']
        return value in valid_values
