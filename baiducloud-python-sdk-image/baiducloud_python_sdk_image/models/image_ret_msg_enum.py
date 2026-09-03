"""
ImageRetMsgEnum information
"""


class ImageRetMsgEnum:
    """
    Enum class for ImageRetMsgEnum
    Allowed values: SUCCESS, PROCESSING
    """

    SUCCESS = 'success'
    PROCESSING = 'processing'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['success', 'processing']
        return value in valid_values
