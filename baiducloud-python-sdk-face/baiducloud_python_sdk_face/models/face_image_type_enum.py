"""
FaceImageTypeEnum information
"""


class FaceImageTypeEnum:
    """
    Enum class for FaceImageTypeEnum
    Allowed values: BASE64, FACE_TOKEN
    """

    BASE64 = 'BASE64'
    FACE_TOKEN = 'FACE_TOKEN'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['BASE64', 'FACE_TOKEN']
        return value in valid_values
