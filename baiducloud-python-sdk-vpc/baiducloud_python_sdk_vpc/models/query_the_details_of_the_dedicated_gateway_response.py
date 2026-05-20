"""
Request entity for QueryTheDetailsOfTheDedicatedGatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class QueryTheDetailsOfTheDedicatedGatewayResponse(BceResponse):
    """
    QueryTheDetailsOfTheDedicatedGatewayResponse
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
        health_check_source_ip=None,
        health_check_dest_ip=None,
        health_check_interval=None,
        health_threshold=None,
        unhealth_threshold=None,
        health_check_type=None,
        health_check_port=None,
        tags=None,
    ):
        """
        Initialize QueryTheDetailsOfTheDedicatedGatewayResponse response.

        :param et_gateway_id: 专线网关的ID
        :type et_gateway_id: str (optional)

        :param name: 专线网关的名称
        :type name: str (optional)

        :param status: 专线网关的状态
        :type status: str (optional)

        :param speed: 专线网关带宽的限速值，单位为Mbps
        :type speed: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param description: 专线网关的描述
        :type description: str (optional)

        :param vpc_id: 专线网关所属VPC的ID
        :type vpc_id: str (optional)

        :param et_id: 绑定的物理专线的ID
        :type et_id: str (optional)

        :param channel_id: 绑定的专线通道的ID
        :type channel_id: str (optional)

        :param local_cidrs: 专线网关的IPv4云端网络
        :type local_cidrs: List[str] (optional)

        :param enable_ipv6: IPv6功能是否开启，1是0否
        :type enable_ipv6: int (optional)

        :param ipv6_local_cidrs: 专线网关的IPv6云端网络
        :type ipv6_local_cidrs: List[str] (optional)

        :param health_check_source_ip: 健康检查的源IP
        :type health_check_source_ip: str (optional)

        :param health_check_dest_ip: 健康检查的目的IP
        :type health_check_dest_ip: str (optional)

        :param health_check_interval: 健康检查的间隔
        :type health_check_interval: int (optional)

        :param health_threshold: 健康的阈值
        :type health_threshold: int (optional)

        :param unhealth_threshold: 不健康的阈值
        :type unhealth_threshold: int (optional)

        :param health_check_type: 健康检查的方式
        :type health_check_type: str (optional)

        :param health_check_port: 健康检查的端口
        :type health_check_port: int (optional)

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
        self.health_check_source_ip = health_check_source_ip
        self.health_check_dest_ip = health_check_dest_ip
        self.health_check_interval = health_check_interval
        self.health_threshold = health_threshold
        self.unhealth_threshold = unhealth_threshold
        self.health_check_type = health_check_type
        self.health_check_port = health_check_port
        self.tags = tags

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
        if self.health_check_source_ip is not None:
            result['healthCheckSourceIp'] = self.health_check_source_ip
        if self.health_check_dest_ip is not None:
            result['healthCheckDestIp'] = self.health_check_dest_ip
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.health_threshold is not None:
            result['healthThreshold'] = self.health_threshold
        if self.unhealth_threshold is not None:
            result['unhealthThreshold'] = self.unhealth_threshold
        if self.health_check_type is not None:
            result['healthCheckType'] = self.health_check_type
        if self.health_check_port is not None:
            result['healthCheckPort'] = self.health_check_port
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryTheDetailsOfTheDedicatedGatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
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
        if m.get('healthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('healthCheckSourceIp')
        if m.get('healthCheckDestIp') is not None:
            self.health_check_dest_ip = m.get('healthCheckDestIp')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('healthThreshold') is not None:
            self.health_threshold = m.get('healthThreshold')
        if m.get('unhealthThreshold') is not None:
            self.unhealth_threshold = m.get('unhealthThreshold')
        if m.get('healthCheckType') is not None:
            self.health_check_type = m.get('healthCheckType')
        if m.get('healthCheckPort') is not None:
            self.health_check_port = m.get('healthCheckPort')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
