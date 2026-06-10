"""
StorageType information
"""


class StorageType:
    """
    Enum class for StorageType
    """

    ENHANCED_SSD_PL0 = 'enhanced_ssd_pl0'
    ENHANCED_SSD_PL1 = 'enhanced_ssd_pl1'
    SSD_ENHANCED = 'SSD_Enhanced'
    ENHANCED_SSD_PL2 = 'enhanced_ssd_pl2'
    ENHANCED_SSD_PL3 = 'enhanced_ssd_pl3'
    CLOUD_HP1 = 'cloud_hp1'
    PREMIUM_SSD = 'premium_ssd'
    HP1 = 'hp1'
    SSD = 'ssd'
    HDD = 'hdd'
    ELASTIC_EPHEMERAL_DISK = 'elastic_ephemeral_disk'
    LOCAL = 'local'
    SATA = 'sata'
    LOCAL_SSD = 'local_ssd'
    LOCAL_HDD = 'local_hdd'
    STD1 = 'std1'
    LOCAL_NVME = 'local_nvme'
    NVME = 'nvme'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = [
            'enhanced_ssd_pl0',
            'enhanced_ssd_pl1',
            'SSD_Enhanced',
            'enhanced_ssd_pl2',
            'enhanced_ssd_pl3',
            'cloud_hp1',
            'premium_ssd',
            'hp1',
            'ssd',
            'hdd',
            'elastic_ephemeral_disk',
            'local',
            'sata',
            'local_ssd',
            'local_hdd',
            'std1',
            'local_nvme',
            'nvme',
        ]
        return value in valid_values
