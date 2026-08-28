"""
VehicleLicenseTypeEnum information
"""


class VehicleLicenseTypeEnum:
    """
    Enum class for VehicleLicenseTypeEnum
    Allowed values: VEHICLE_FRONT, VEHICLE_BACK, DRIVING_FRONT, DRIVING_BACK
    """

    VEHICLE_FRONT = 'vehicle_front'
    VEHICLE_BACK = 'vehicle_back'
    DRIVING_FRONT = 'driving_front'
    DRIVING_BACK = 'driving_back'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['vehicle_front', 'vehicle_back', 'driving_front', 'driving_back']
        return value in valid_values
