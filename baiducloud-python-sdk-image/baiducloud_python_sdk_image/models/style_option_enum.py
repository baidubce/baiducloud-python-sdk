"""
StyleOptionEnum information
"""


class StyleOptionEnum:
    """
    Enum class for StyleOptionEnum
    Allowed values: CARTOON, PENCIL, COLOR_PENCIL, WARM, WAVE, LAVENDER, MONONOKE, SCREAM, GOTHIC
    """

    CARTOON = 'cartoon'
    PENCIL = 'pencil'
    COLOR_PENCIL = 'color_pencil'
    WARM = 'warm'
    WAVE = 'wave'
    LAVENDER = 'lavender'
    MONONOKE = 'mononoke'
    SCREAM = 'scream'
    GOTHIC = 'gothic'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'cartoon',
            'pencil',
            'color_pencil',
            'warm',
            'wave',
            'lavender',
            'mononoke',
            'scream',
            'gothic',
        ]
        return value in valid_values
