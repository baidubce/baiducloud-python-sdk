"""
Request entity for ZoneMigrationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.subnet_map import SubnetMap


class ZoneMigrationRequest(AbstractModel):
    """
    Request entity for ZoneMigrationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, master__azone, backup__azone, zone_names, subnets, effective_time):
        """
        Initialize ZoneMigrationRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param master__azone: 主可用区
        :type master__azone: str (required)

        :param backup__azone: 备可用区
        :type backup__azone: str (required)

        :param zone_names: 可用区
        :type zone_names: List[str] (required)

        :param subnets: 可用区子网
        :type subnets: List[SubnetMap] (required)

        :param effective_time: effective_time parameter
        :type effective_time: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.master__azone = master__azone
        self.backup__azone = backup__azone
        self.zone_names = zone_names
        self.subnets = subnets
        self.effective_time = effective_time

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.master__azone is not None:
            result['master\_azone'] = self.master__azone
        if self.backup__azone is not None:
            result['backup\_azone'] = self.backup__azone
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ZoneMigrationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('master\_azone') is not None:
            self.master__azone = m.get('master\_azone')
        if m.get('backup\_azone') is not None:
            self.backup__azone = m.get('backup\_azone')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('subnets') is not None:
            self.subnets = [SubnetMap().from_dict(i) for i in m.get('subnets')]
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')
        return self
