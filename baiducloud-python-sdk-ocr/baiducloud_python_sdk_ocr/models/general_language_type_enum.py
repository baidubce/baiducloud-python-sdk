"""
GeneralLanguageTypeEnum information
"""


class GeneralLanguageTypeEnum:
    """
    Enum class for GeneralLanguageTypeEnum
    Allowed values: CHN_ENG, ENG, JAP, KOR, FRE, SPA, POR, GER, ITA, RUS
    """

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

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['CHN_ENG', 'ENG', 'JAP', 'KOR', 'FRE', 'SPA', 'POR', 'GER', 'ITA', 'RUS']
        return value in valid_values
