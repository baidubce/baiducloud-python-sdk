"""
BusinessLicenseRiskTypeEnum information
"""


class BusinessLicenseRiskTypeEnum:
    """
    Enum class for BusinessLicenseRiskTypeEnum
    Allowed values: NORMAL, COPY, SCREEN, SCAN
    """

    NORMAL = 'normal'
    COPY = 'copy'
    SCREEN = 'screen'
    SCAN = 'scan'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['normal', 'copy', 'screen', 'scan']
        return value in valid_values
