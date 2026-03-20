"""
InstanceType information
"""


class InstanceType:
    """
    Enum class for InstanceType
    Allowed values: BCC, BBC, DCC, ENI, BLB, VPN, NAT
    """

    BCC = 'BCC'
    BBC = 'BBC'
    DCC = 'DCC'
    ENI = 'ENI'
    BLB = 'BLB'
    VPN = 'VPN'
    NAT = 'NAT'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['BCC', 'BBC', 'DCC', 'ENI', 'BLB', 'VPN', 'NAT']
        return value in valid_values
