"""
VatInvoiceTypeEnum information
"""


class VatInvoiceTypeEnum:
    """
    Enum class for VatInvoiceTypeEnum
    Allowed values: NORMAL, ROLL
    """

    NORMAL = 'normal'
    ROLL = 'roll'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['normal', 'roll']
        return value in valid_values
