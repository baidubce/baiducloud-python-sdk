"""
Execution information
"""


class Execution:
    """
    Enum class for Execution
    Allowed values: SAVE, RUN, SAVE_AND_RUN
    """

    SAVE = 'SAVE'
    RUN = 'RUN'
    SAVE_AND_RUN = 'SAVE_AND_RUN'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['SAVE', 'RUN', 'SAVE_AND_RUN']
        return value in valid_values
