"""
PeriodType information
"""


class PeriodType:
    """
    Enum class for PeriodType
    Allowed values: DAY, WEEK, MONTH, CRONEXPRESSION
    """

    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    CRONEXPRESSION = 'CronExpression'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['DAY', 'WEEK', 'MONTH', 'CronExpression']
        return value in valid_values
