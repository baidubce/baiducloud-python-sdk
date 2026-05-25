"""
Request entity for QueryTheSpecifiedIpAddressFamilyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.ip_collection_binded_instance import IpCollectionBindedInstance


class QueryTheSpecifiedIpAddressFamilyResponse(BceResponse):
    """
    QueryTheSpecifiedIpAddressFamilyResponse
    """

    def __init__(
        self, ip_group_id=None, name=None, description=None, ip_version=None, ip_set_ids=None, binded_instances=None
    ):
        """
        Initialize QueryTheSpecifiedIpAddressFamilyResponse response.

        :param ip_group_id: IP地址族的ID
        :type ip_group_id: str (optional)

        :param name: IP地址组的名称
        :type name: str (optional)

        :param description: IP地址组的描述
        :type description: str (optional)

        :param ip_version: ipVersion，取值IPv4或IPv6
        :type ip_version: str (optional)

        :param ip_set_ids: 关联的IP地址组ID列表
        :type ip_set_ids: List[str] (optional)

        :param binded_instances: IP地址族绑定的实例
        :type binded_instances: List[IpCollectionBindedInstance] (optional)
        """
        super().__init__()
        self.ip_group_id = ip_group_id
        self.name = name
        self.description = description
        self.ip_version = ip_version
        self.ip_set_ids = ip_set_ids
        self.binded_instances = binded_instances

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.ip_group_id is not None:
            result['ipGroupId'] = self.ip_group_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.ip_set_ids is not None:
            result['ipSetIds'] = self.ip_set_ids
        if self.binded_instances is not None:
            result['bindedInstances'] = [i.to_dict() for i in self.binded_instances]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryTheSpecifiedIpAddressFamilyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('ipSetIds') is not None:
            self.ip_set_ids = m.get('ipSetIds')
        if m.get('bindedInstances') is not None:
            self.binded_instances = [IpCollectionBindedInstance().from_dict(i) for i in m.get('bindedInstances')]
        return self
