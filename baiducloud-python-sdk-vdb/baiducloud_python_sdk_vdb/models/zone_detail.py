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
        api_zone_names=None,
        available=None,
        default_subnet_id=None,
        max_cpu_count=None,
        max_memory=None,
        max_storage=None,
        stock_state=None,
        zone_name_str=None,
        zone_names=None,
    ):
        """
        Initialize ZoneDetail instance.

        :param api_zone_names:
        :type api_zone_names: List[str] (optional)

        :param available:
        :type available: bool (optional)

        :param default_subnet_id:
        :type default_subnet_id: str (optional)

        :param max_cpu_count:
        :type max_cpu_count: int (optional)

        :param max_memory:
        :type max_memory: int (optional)

        :param max_storage:
        :type max_storage: int (optional)

        :param stock_state:
        :type stock_state: int (optional)

        :param zone_name_str:
        :type zone_name_str: str (optional)

        :param zone_names:
        :type zone_names: List[str] (optional)
        """
        super().__init__()
        self.api_zone_names = api_zone_names
        self.available = available
        self.default_subnet_id = default_subnet_id
        self.max_cpu_count = max_cpu_count
        self.max_memory = max_memory
        self.max_storage = max_storage
        self.stock_state = stock_state
        self.zone_name_str = zone_name_str
        self.zone_names = zone_names

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
        if self.api_zone_names is not None:
            result['apiZoneNames'] = self.api_zone_names
        if self.available is not None:
            result['available'] = self.available
        if self.default_subnet_id is not None:
            result['defaultSubnetId'] = self.default_subnet_id
        if self.max_cpu_count is not None:
            result['maxCpuCount'] = self.max_cpu_count
        if self.max_memory is not None:
            result['maxMemory'] = self.max_memory
        if self.max_storage is not None:
            result['maxStorage'] = self.max_storage
        if self.stock_state is not None:
            result['stockState'] = self.stock_state
        if self.zone_name_str is not None:
            result['zoneNameStr'] = self.zone_name_str
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
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
        if m.get('apiZoneNames') is not None:
            self.api_zone_names = m.get('apiZoneNames')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('defaultSubnetId') is not None:
            self.default_subnet_id = m.get('defaultSubnetId')
        if m.get('maxCpuCount') is not None:
            self.max_cpu_count = m.get('maxCpuCount')
        if m.get('maxMemory') is not None:
            self.max_memory = m.get('maxMemory')
        if m.get('maxStorage') is not None:
            self.max_storage = m.get('maxStorage')
        if m.get('stockState') is not None:
            self.stock_state = m.get('stockState')
        if m.get('zoneNameStr') is not None:
            self.zone_name_str = m.get('zoneNameStr')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        return self
