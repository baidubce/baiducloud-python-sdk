"""
Request entity for CreateResolverRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_privatezone.models.ip_model import IpModel


class CreateResolverRequest(AbstractModel):
    """
    Request entity for CreateResolverRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, vpc_id, vpc_region, ip_models, type, client_token=None, description=None):
        """
        Initialize CreateResolverRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 解析器名称，允许大小写字母、数字、中文以及-_/.特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (required)

        :param description: 解析器描述，不超过200字符
        :type description: str (optional)

        :param vpc_id: 解析器所在的vpc的id
        :type vpc_id: str (required)

        :param vpc_region: 解析器所在的地区
        :type vpc_region: str (required)

        :param ip_models: 入站/出站的流量地址
        :type ip_models: List[IpModel] (required)

        :param type: 解析器类型，描述：outbound：出站解析器；inbound：入站解析器
        :type type: str (required)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.vpc_id = vpc_id
        self.vpc_region = vpc_region
        self.ip_models = ip_models
        self.type = type

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_region is not None:
            result['vpcRegion'] = self.vpc_region
        if self.ip_models is not None:
            result['ipModels'] = [i.to_dict() for i in self.ip_models]
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateResolverRequest

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
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcRegion') is not None:
            self.vpc_region = m.get('vpcRegion')
        if m.get('ipModels') is not None:
            self.ip_models = [IpModel().from_dict(i) for i in m.get('ipModels')]
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
