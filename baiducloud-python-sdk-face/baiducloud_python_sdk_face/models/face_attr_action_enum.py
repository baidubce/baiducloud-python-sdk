"""
FaceAttrActionEnum information
"""


class FaceAttrActionEnum:
    """
    Enum class for FaceAttrActionEnum
    Allowed values: TO_KID, TO_OLD, TO_FEMALE, TO_MALE, V2_AGE, V2_GENDER
    """

    TO_KID = 'TO_KID'
    TO_OLD = 'TO_OLD'
    TO_FEMALE = 'TO_FEMALE'
    TO_MALE = 'TO_MALE'
    V2_AGE = 'V2_AGE'
    V2_GENDER = 'V2_GENDER'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['TO_KID', 'TO_OLD', 'TO_FEMALE', 'TO_MALE', 'V2_AGE', 'V2_GENDER']
        return value in valid_values
