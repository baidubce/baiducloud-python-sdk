"""
TargetSelectorType information
"""


class TargetSelectorType:
    """
    Enum class for TargetSelectorType
    Allowed values: INSTANCES_LIST, ALL_INSTANCES, TAG_INSTANCES, INSTANCES_IMPORT
    """

    INSTANCES_LIST = 'INSTANCES_LIST'
    ALL_INSTANCES = 'ALL_INSTANCES'
    TAG_INSTANCES = 'TAG_INSTANCES'
    INSTANCES_IMPORT = 'INSTANCES_IMPORT'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['INSTANCES_LIST', 'ALL_INSTANCES', 'TAG_INSTANCES', 'INSTANCES_IMPORT']
        return value in valid_values
