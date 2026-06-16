"""
ProductType information
"""


class ProductType:
    """
    Enum class for ProductType
    Allowed values: PREPAID, POSTPAID
    """

    PREPAID = 'Prepaid'
    POSTPAID = 'Postpaid'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['Prepaid', 'Postpaid']
        return value in valid_values
