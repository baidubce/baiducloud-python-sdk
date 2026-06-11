"""
ImageType information
"""


class ImageType:
    """
    Enum class for ImageType
    """

    ALL = 'All'
    SYSTEM = 'System'
    CUSTOM = 'Custom'
    INTEGRATION = 'Integration'
    SHARING = 'Sharing'
    BBCSYSTEM = 'BbcSystem'
    BBCCUSTOM = 'BbcCustom'
    GPUBCCSYSTEM = 'GpuBccSystem'
    GPUBCCCUSTOM = 'GpuBccCustom'
    GPUBBCSYSTEM = 'GpuBbcSystem'
    GPUBBCCUSTOM = 'GpuBbcCustom'
    EBCTOTAL = 'EbcTotal'
    EBCSYSTEM = 'EbcSystem'
    EBCCUSTOM = 'EbcCustom'
    FPGABCCSYSTEM = 'FpgaBccSystem'
    FPGABCCCUSTOM = 'FpgaBccCustom'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'All',
            'System',
            'Custom',
            'Integration',
            'Sharing',
            'BbcSystem',
            'BbcCustom',
            'GpuBccSystem',
            'GpuBccCustom',
            'GpuBbcSystem',
            'GpuBbcCustom',
            'EbcTotal',
            'EbcSystem',
            'EbcCustom',
            'FpgaBccSystem',
            'FpgaBccCustom',
        ]
        return value in valid_values
