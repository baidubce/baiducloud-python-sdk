"""
PaddleVlParserTaskStatusEnum information
"""


class PaddleVlParserTaskStatusEnum:
    """
    Enum class for PaddleVlParserTaskStatusEnum
    Allowed values: PENDING, PROCESSING, SUCCESS, FAILED
    """

    PENDING = 'pending'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILED = 'failed'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['pending', 'processing', 'success', 'failed']
        return value in valid_values
