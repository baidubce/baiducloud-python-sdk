"""
Request entity for CreateDedicatedGatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateDedicatedGatewayRequest(AbstractModel):
    """
    Request entity for CreateDedicatedGatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        vpc_id,
        speed,
        client_token=None,
        description=None,
        et_id=None,
        channel_id=None,
        local_cidrs=None,
        tags=None,
        resource_group_id=None,
    ):
        """
        Initialize CreateDedicatedGatewayRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 专线网关的名称，由大小写字母、数字以及-_ /.特殊字符组成，必须以字母开头，长度1-65
        :type name: str (required)

        :param vpc_id: 专线网关所属VPC的ID
        :type vpc_id: str (required)

        :param speed: 专线网关带宽的限速值，单位为Mbps。限制为为2~10000之间的整数
        :type speed: int (required)

        :param description: 专线网关的描述，不超过200字符
        :type description: str (optional)

        :param et_id: 绑定的物理专线的ID，etid和channelId必须同时存在
        :type et_id: str (optional)

        :param channel_id: 绑定的专线通道的ID，etid和channelId必须同时存在
        :type channel_id: str (optional)

        :param local_cidrs: 专线网关的云端网络，用户可以选本vpc网段或自定义一个或多个网段，仅当参数etId和channelId存在时可以设置
        :type local_cidrs: List[str] (optional)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 资源组
        :type resource_group_id: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.vpc_id = vpc_id
        self.speed = speed
        self.description = description
        self.et_id = et_id
        self.channel_id = channel_id
        self.local_cidrs = local_cidrs
        self.tags = tags
        self.resource_group_id = resource_group_id

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.speed is not None:
            result['speed'] = self.speed
        if self.description is not None:
            result['description'] = self.description
        if self.et_id is not None:
            result['etId'] = self.et_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.local_cidrs is not None:
            result['localCidrs'] = self.local_cidrs
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDedicatedGatewayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('localCidrs') is not None:
            self.local_cidrs = m.get('localCidrs')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self
