"""
AccurateLanguageTypeExEnum information
"""


class AccurateLanguageTypeExEnum:
    """
    Enum class for AccurateLanguageTypeExEnum
    """

    AUTO_DETECT = 'auto_detect'
    CHN_ENG = 'CHN_ENG'
    ENG = 'ENG'
    JAP = 'JAP'
    KOR = 'KOR'
    FRE = 'FRE'
    SPA = 'SPA'
    POR = 'POR'
    GER = 'GER'
    ITA = 'ITA'
    RUS = 'RUS'
    DAN = 'DAN'
    DUT = 'DUT'
    MAL = 'MAL'
    SWE = 'SWE'
    IND = 'IND'
    POL = 'POL'
    ROM = 'ROM'
    TUR = 'TUR'
    GRE = 'GRE'
    HUN = 'HUN'
    THA = 'THA'
    VIE = 'VIE'
    ARA = 'ARA'
    HIN = 'HIN'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'auto_detect',
            'CHN_ENG',
            'ENG',
            'JAP',
            'KOR',
            'FRE',
            'SPA',
            'POR',
            'GER',
            'ITA',
            'RUS',
            'DAN',
            'DUT',
            'MAL',
            'SWE',
            'IND',
            'POL',
            'ROM',
            'TUR',
            'GRE',
            'HUN',
            'THA',
            'VIE',
            'ARA',
            'HIN',
        ]
        return value in valid_values
