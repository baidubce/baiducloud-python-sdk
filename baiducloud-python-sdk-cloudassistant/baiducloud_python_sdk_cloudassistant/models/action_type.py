"""
ActionType information
"""


class ActionType:
    """
    Enum class for ActionType
    Allowed values: COMMAND, FILE_UPLOAD
    """

    COMMAND = 'COMMAND'
    FILE_UPLOAD = 'FILE_UPLOAD'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['COMMAND', 'FILE_UPLOAD']
        return value in valid_values
