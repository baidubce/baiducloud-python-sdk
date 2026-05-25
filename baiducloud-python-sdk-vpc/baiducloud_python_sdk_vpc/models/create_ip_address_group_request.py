"""
Request entity for CreateIpAddressGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.template_ip_address_info import TemplateIpAddressInfo


class CreateIpAddressGroupRequest(AbstractModel):
    """
    Request entity for CreateIpAddressGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, ip_version, ip_address_info, client_token=None, description=None):
        """
        Initialize CreateIpAddressGroupRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: IP地址组的名称，限制：大小写字母、数字、中文以及-_/.特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (required)

        :param ip_version: ipVersion，取值IPv4或IPv6
        :type ip_version: str (required)

        :param ip_address_info: 参数模板IP地址信息，单次最多指定10个
        :type ip_address_info: List[TemplateIpAddressInfo] (required)

        :param description: IP地址组描述，长度不超过255
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.ip_version = ip_version
        self.ip_address_info = ip_address_info
        self.description = description

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
        if self.name is not None:
            result['name'] = self.name
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.ip_address_info is not None:
            result['ipAddressInfo'] = [i.to_dict() for i in self.ip_address_info]
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIpAddressGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('ipAddressInfo') is not None:
            self.ip_address_info = [TemplateIpAddressInfo().from_dict(i) for i in m.get('ipAddressInfo')]
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
