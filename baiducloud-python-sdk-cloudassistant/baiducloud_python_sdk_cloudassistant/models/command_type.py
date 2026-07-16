"""
CommandType information
"""


class CommandType:
    """
    Enum class for CommandType
    Allowed values: SHELL, POWERSHELL
    """

    SHELL = 'SHELL'
    POWERSHELL = 'POWERSHELL'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['SHELL', 'POWERSHELL']
        return value in valid_values
