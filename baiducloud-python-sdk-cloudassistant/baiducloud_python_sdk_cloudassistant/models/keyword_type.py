"""
KeywordType information
"""


class KeywordType:
    """
    Enum class for KeywordType
    Allowed values: INSTANCEID, INTERNALIP
    """

    INSTANCEID = 'instanceId'
    INTERNALIP = 'internalIp'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['instanceId', 'internalIp']
        return value in valid_values
