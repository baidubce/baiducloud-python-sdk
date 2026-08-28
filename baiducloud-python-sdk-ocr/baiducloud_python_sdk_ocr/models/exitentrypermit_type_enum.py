"""
ExitentrypermitTypeEnum information
"""


class ExitentrypermitTypeEnum:
    """
    Enum class for ExitentrypermitTypeEnum
    """

    HK_MC_PASSPORT_FRONT = 'hk_mc_passport_front'
    HK_MC_PASSPORT_BACK = 'hk_mc_passport_back'
    TW_PASSPORT_FRONT = 'tw_passport_front'
    TW_PASSPORT_BACK = 'tw_passport_back'
    TW_RETURN_PASSPORT_FRONT = 'tw_return_passport_front'
    TW_RETURN_PASSPORT_BACK = 'tw_return_passport_back'
    HK_MC_RETURN_PASSPORT_FRONT = 'hk_mc_return_passport_front'
    HK_MC_RETURN_PASSPORT_BACK = 'hk_mc_return_passport_back'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'hk_mc_passport_front',
            'hk_mc_passport_back',
            'tw_passport_front',
            'tw_passport_back',
            'tw_return_passport_front',
            'tw_return_passport_back',
            'hk_mc_return_passport_front',
            'hk_mc_return_passport_back',
        ]
        return value in valid_values
