"""
FaceTypeEnum information
"""


class FaceTypeEnum:
    """
    Enum class for FaceTypeEnum
    Allowed values: LIVE, IDCARD, WATERMARK, CERT, INFRARED, HYBRID
    """

    LIVE = 'LIVE'
    IDCARD = 'IDCARD'
    WATERMARK = 'WATERMARK'
    CERT = 'CERT'
    INFRARED = 'INFRARED'
    HYBRID = 'HYBRID'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['LIVE', 'IDCARD', 'WATERMARK', 'CERT', 'INFRARED', 'HYBRID']
        return value in valid_values
