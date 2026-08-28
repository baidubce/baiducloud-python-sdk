"""
BarcodeTypeEnum information
"""


class BarcodeTypeEnum:
    """
    Enum class for BarcodeTypeEnum
    """

    UPC_A = 'UPC_A'
    UPC_E = 'UPC_E'
    EAN_13 = 'EAN_13'
    EAN_8 = 'EAN_8'
    CODE_39 = 'CODE_39'
    CODE_93 = 'CODE_93'
    CODE_128 = 'CODE_128'
    ITF = 'ITF'
    CODABAR = 'CODABAR'
    QR_CODE = 'QR_CODE'
    DATA_MATRIX = 'DATA_MATRIX'
    AZTEC = 'AZTEC'
    PDF_417 = 'PDF_417'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'UPC_A',
            'UPC_E',
            'EAN_13',
            'EAN_8',
            'CODE_39',
            'CODE_93',
            'CODE_128',
            'ITF',
            'CODABAR',
            'QR_CODE',
            'DATA_MATRIX',
            'AZTEC',
            'PDF_417',
        ]
        return value in valid_values
