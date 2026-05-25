"""
EtGateway information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class EtGateway(AbstractModel):
    """
    EtGateway
    """

    def __init__(
        self,
        et_gateway_id=None,
        name=None,
        status=None,
        speed=None,
        create_time=None,
        description=None,
        vpc_id=None,
        et_id=None,
        channel_id=None,
        local_cidrs=None,
        enable_ipv6=None,
        ipv6_local_cidrs=None,
        tags=None,
    ):
        """
        Initialize EtGateway instance.

        :param et_gateway_id: 专线网关id
        :type et_gateway_id: str (optional)

        :param name: 专线网关名称
        :type name: str (optional)

        :param status: 专线网关状态
        :type status: str (optional)

        :param speed: 出口带宽
        :type speed: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param description: 专线网关描述
        :type description: str (optional)

        :param vpc_id: 虚拟网络id
        :type vpc_id: str (optional)

        :param et_id: 专线id
        :type et_id: str (optional)

        :param channel_id: 专线通道id
        :type channel_id: str (optional)

        :param local_cidrs: IPv4云端网络
        :type local_cidrs: List[str] (optional)

        :param enable_ipv6: IPv6功能是否开启，1是0否
        :type enable_ipv6: int (optional)

        :param ipv6_local_cidrs: IPv6云端网络
        :type ipv6_local_cidrs: List[str] (optional)

        :param tags: 专线网关绑定的标签集合
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.et_gateway_id = et_gateway_id
        self.name = name
        self.status = status
        self.speed = speed
        self.create_time = create_time
        self.description = description
        self.vpc_id = vpc_id
        self.et_id = et_id
        self.channel_id = channel_id
        self.local_cidrs = local_cidrs
        self.enable_ipv6 = enable_ipv6
        self.ipv6_local_cidrs = ipv6_local_cidrs
        self.tags = tags

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
        if self.et_gateway_id is not None:
            result['etGatewayId'] = self.et_gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.speed is not None:
            result['speed'] = self.speed
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.et_id is not None:
            result['etId'] = self.et_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.local_cidrs is not None:
            result['localCidrs'] = self.local_cidrs
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.ipv6_local_cidrs is not None:
            result['ipv6LocalCidrs'] = self.ipv6_local_cidrs
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EtGateway

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etGatewayId') is not None:
            self.et_gateway_id = m.get('etGatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('localCidrs') is not None:
            self.local_cidrs = m.get('localCidrs')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('ipv6LocalCidrs') is not None:
            self.ipv6_local_cidrs = m.get('ipv6LocalCidrs')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
