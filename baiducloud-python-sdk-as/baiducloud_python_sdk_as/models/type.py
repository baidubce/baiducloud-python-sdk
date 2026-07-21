"""
Type information
"""


class Type:
    """
    Enum class for Type
    Allowed values: CRONTAB, PERIOD, ALARM
    """

    CRONTAB = 'CRONTAB'
    PERIOD = 'PERIOD'
    ALARM = 'ALARM'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['CRONTAB', 'PERIOD', 'ALARM']
        return value in valid_values
