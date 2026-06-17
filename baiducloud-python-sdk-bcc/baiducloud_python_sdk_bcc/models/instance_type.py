"""
InstanceType information
"""


class InstanceType:
    """
    Enum class for InstanceType
    Allowed values: N1, N2, N3, N4, N5, N6, C1, C2, S1, G1, F1
    """

    N1 = 'N1'
    N2 = 'N2'
    N3 = 'N3'
    N4 = 'N4'
    N5 = 'N5'
    N6 = 'N6'
    C1 = 'C1'
    C2 = 'C2'
    S1 = 'S1'
    G1 = 'G1'
    F1 = 'F1'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'C1', 'C2', 'S1', 'G1', 'F1']
        return value in valid_values
