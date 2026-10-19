"""
ZoneDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ZoneDetail(AbstractModel):
    """
    ZoneDetail
    """

    def __init__(
        self,
        zone_names=None,
        api_zone_names=None,
        available=None,
        zone_name_str=None,
        default_subnet_id=None,
        max_cpu_count=None,
        max_memory=None,
        max_storage=None,
        support_nvme_disk=None,
        zone_type=None,
    ):
        """
        Initialize ZoneDetail instance.

        :param zone_names: 可用区名称的列表，显示当前的可用区名称
        :type zone_names: List[str] (optional)

        :param api_zone_names: api可用区名称列表，显示当前的可用区名称，这个字段属于openApi专属字段
        :type api_zone_names: List[str] (optional)

        :param available: 可用区状态：true(可用) ， false(不可用)
        :type available: bool (optional)

        :param zone_name_str: 当前可用区名称
        :type zone_name_str: str (optional)

        :param default_subnet_id: 默认子网ID
        :type default_subnet_id: str (optional)

        :param max_cpu_count: 可用区，统计最大CPU数
        :type max_cpu_count: int (optional)

        :param max_memory: 可用区，最大内存容量
        :type max_memory: int (optional)

        :param max_storage: 可用区，最大磁盘存储容量
        :type max_storage: int (optional)

        :param support_nvme_disk: 是否支持Nvme磁盘。 true（支持），false（不支持）
        :type support_nvme_disk: bool (optional)

        :param zone_type: 可用区类型，例如 normal
        :type zone_type: str (optional)
        """
        super().__init__()
        self.zone_names = zone_names
        self.api_zone_names = api_zone_names
        self.available = available
        self.zone_name_str = zone_name_str
        self.default_subnet_id = default_subnet_id
        self.max_cpu_count = max_cpu_count
        self.max_memory = max_memory
        self.max_storage = max_storage
        self.support_nvme_disk = support_nvme_disk
        self.zone_type = zone_type

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.api_zone_names is not None:
            result['apiZoneNames'] = self.api_zone_names
        if self.available is not None:
            result['available'] = self.available
        if self.zone_name_str is not None:
            result['zoneNameStr'] = self.zone_name_str
        if self.default_subnet_id is not None:
            result['defaultSubnetId'] = self.default_subnet_id
        if self.max_cpu_count is not None:
            result['maxCpuCount'] = self.max_cpu_count
        if self.max_memory is not None:
            result['maxMemory'] = self.max_memory
        if self.max_storage is not None:
            result['maxStorage'] = self.max_storage
        if self.support_nvme_disk is not None:
            result['supportNvmeDisk'] = self.support_nvme_disk
        if self.zone_type is not None:
            result['zoneType'] = self.zone_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ZoneDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('apiZoneNames') is not None:
            self.api_zone_names = m.get('apiZoneNames')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('zoneNameStr') is not None:
            self.zone_name_str = m.get('zoneNameStr')
        if m.get('defaultSubnetId') is not None:
            self.default_subnet_id = m.get('defaultSubnetId')
        if m.get('maxCpuCount') is not None:
            self.max_cpu_count = m.get('maxCpuCount')
        if m.get('maxMemory') is not None:
            self.max_memory = m.get('maxMemory')
        if m.get('maxStorage') is not None:
            self.max_storage = m.get('maxStorage')
        if m.get('supportNvmeDisk') is not None:
            self.support_nvme_disk = m.get('supportNvmeDisk')
        if m.get('zoneType') is not None:
            self.zone_type = m.get('zoneType')
        return self
