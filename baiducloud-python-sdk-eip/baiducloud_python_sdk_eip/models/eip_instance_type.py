
class EipInstanceType:
    """
    Enum class for EipInstanceType
    Allowed values: NORMAL, SHARED
    """
    NORMAL = 'normal'
    SHARED = 'shared'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['normal', 'shared']
        return value in valid_values
