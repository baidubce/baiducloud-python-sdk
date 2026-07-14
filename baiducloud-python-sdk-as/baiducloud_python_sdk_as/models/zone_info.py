"""
ZoneInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ZoneInfo(AbstractModel):
    """
    ZoneInfo
    """

    def __init__(
        self, zone=None, subnet_id=None, subnet_uuid=None, subnet_name=None, subnet_type=None, node_count=None
    ):
        """
        Initialize ZoneInfo instance.

        :param zone: 可用区
        :type zone: str (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param subnet_uuid: 子网UUID
        :type subnet_uuid: str (optional)

        :param subnet_name: 子网名称
        :type subnet_name: str (optional)

        :param subnet_type: 子网类型
        :type subnet_type: int (optional)

        :param node_count: 节点数量
        :type node_count: int (optional)
        """
        super().__init__()
        self.zone = zone
        self.subnet_id = subnet_id
        self.subnet_uuid = subnet_uuid
        self.subnet_name = subnet_name
        self.subnet_type = subnet_type
        self.node_count = node_count

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
        if self.zone is not None:
            result['zone'] = self.zone
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.subnet_uuid is not None:
            result['subnetUuid'] = self.subnet_uuid
        if self.subnet_name is not None:
            result['subnetName'] = self.subnet_name
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ZoneInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('subnetUuid') is not None:
            self.subnet_uuid = m.get('subnetUuid')
        if m.get('subnetName') is not None:
            self.subnet_name = m.get('subnetName')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        return self
