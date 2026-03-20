"""
Request entity for CreateVpcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateVpcRequest(AbstractModel):
    """
    Request entity for CreateVpcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, cidr, client_token=None, description=None, enable_ipv6=None, tags=None):
        """
        Initialize CreateVpcRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: VPC名称，不能取值\"default\"，长度不超过65个字符，可由数字，字符，下划线组成
        :type name: str (required)

        :param description: VPC描述，不超过200字符
        :type description: str (optional)

        :param cidr: VPC的cidr
        :type cidr: str (required)

        :param enable_ipv6: 是否开启IPv6网段，true开启，默认false不开启。
        :type enable_ipv6: bool (optional)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.cidr = cidr
        self.enable_ipv6 = enable_ipv6
        self.tags = tags

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
        if self.description is not None:
            result['description'] = self.description
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVpcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
