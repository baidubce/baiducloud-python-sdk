"""
Request entity for QueryTheSpecifiedIpAddressGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.template_ip_address_info import TemplateIpAddressInfo
from baiducloud_python_sdk_vpc.models.ip_collection_binded_instance import IpCollectionBindedInstance


class QueryTheSpecifiedIpAddressGroupResponse(BceResponse):
    """
    QueryTheSpecifiedIpAddressGroupResponse
    """

    def __init__(
        self, ip_set_id=None, name=None, description=None, ip_version=None, ip_address_info=None, binded_instances=None
    ):
        """
        Initialize QueryTheSpecifiedIpAddressGroupResponse response.

        :param ip_set_id: IP地址组的ID
        :type ip_set_id: str (optional)

        :param name: IP地址组的名称
        :type name: str (optional)

        :param description: IP地址组的描述
        :type description: str (optional)

        :param ip_version: ipVersion，取值IPv4或IPv6
        :type ip_version: str (optional)

        :param ip_address_info: 参数模板IP地址信息
        :type ip_address_info: List[TemplateIpAddressInfo] (optional)

        :param binded_instances: IP地址组绑定的实例
        :type binded_instances: List[IpCollectionBindedInstance] (optional)
        """
        super().__init__()
        self.ip_set_id = ip_set_id
        self.name = name
        self.description = description
        self.ip_version = ip_version
        self.ip_address_info = ip_address_info
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
        if self.ip_set_id is not None:
            result['ipSetId'] = self.ip_set_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.ip_address_info is not None:
            result['ipAddressInfo'] = [i.to_dict() for i in self.ip_address_info]
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
        :rtype: QueryTheSpecifiedIpAddressGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipSetId') is not None:
            self.ip_set_id = m.get('ipSetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('ipAddressInfo') is not None:
            self.ip_address_info = [TemplateIpAddressInfo().from_dict(i) for i in m.get('ipAddressInfo')]
        if m.get('bindedInstances') is not None:
            self.binded_instances = [IpCollectionBindedInstance().from_dict(i) for i in m.get('bindedInstances')]
        return self
