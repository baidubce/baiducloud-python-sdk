"""
Type information
"""


class Type:
    """
    Enum class for Type
    Allowed values: CRONTAB, ALARM, PERIOD
    """

    CRONTAB = 'CRONTAB'
    ALARM = 'ALARM'
    PERIOD = 'PERIOD'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['CRONTAB', 'ALARM', 'PERIOD']
        return value in valid_values
