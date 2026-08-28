"""
MultiIdcardImageStatusEnum information
"""


class MultiIdcardImageStatusEnum:
    """
    Enum class for MultiIdcardImageStatusEnum
    Allowed values: NORMAL, REVERSED_SIDE, NON_IDCARD, BLURRED, OTHER_TYPE_CARD, OVER_EXPOSURE, OVER_DARK, UNKNOWN
    """

    NORMAL = 'normal'
    REVERSED_SIDE = 'reversed_side'
    NON_IDCARD = 'non_idcard'
    BLURRED = 'blurred'
    OTHER_TYPE_CARD = 'other_type_card'
    OVER_EXPOSURE = 'over_exposure'
    OVER_DARK = 'over_dark'
    UNKNOWN = 'unknown'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'normal',
            'reversed_side',
            'non_idcard',
            'blurred',
            'other_type_card',
            'over_exposure',
            'over_dark',
            'unknown',
        ]
        return value in valid_values
