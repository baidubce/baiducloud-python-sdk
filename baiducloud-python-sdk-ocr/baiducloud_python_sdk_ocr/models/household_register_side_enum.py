"""
HouseholdRegisterSideEnum information
"""


class HouseholdRegisterSideEnum:
    """
    Enum class for HouseholdRegisterSideEnum
    Allowed values: SUBPAGE, HOMEPAGE
    """

    SUBPAGE = 'subpage'
    HOMEPAGE = 'homepage'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['subpage', 'homepage']
        return value in valid_values
