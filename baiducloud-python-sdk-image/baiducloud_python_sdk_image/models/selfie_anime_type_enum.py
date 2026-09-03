"""
SelfieAnimeTypeEnum information
"""


class SelfieAnimeTypeEnum:
    """
    Enum class for SelfieAnimeTypeEnum
    Allowed values: ANIME, ANIME_MASK
    """

    ANIME = 'anime'
    ANIME_MASK = 'anime_mask'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['anime', 'anime_mask']
        return value in valid_values
