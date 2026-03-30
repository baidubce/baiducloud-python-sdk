"""
Request entity for CreateGatewayLimitRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateGatewayLimitRulesRequest(AbstractModel):
    """
    Request entity for CreateGatewayLimitRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        ip_version,
        name,
        service_type,
        resource_id,
        direction,
        cidr,
        bandwidth,
        client_token=None,
        description=None,
        sub_service_type=None,
        peer_region=None,
    ):
        """
        Initialize CreateGatewayLimitRulesRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_version: IP协议版本,当前取值4
        :type ip_version: str (required)

        :param name: 规则名称,需满足名称规则。支持大小写字母、数字以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type name: str (required)

        :param description: 描述信息。长度0-200
        :type description: str (optional)

        :param service_type: 服务类型(peerconn,et,csn)<br/>peerconn-对等连接<br/>et-专线网关<br/>csn-云智能网
        :type service_type: str (required)

        :param sub_service_type:
            子服务类型，当serviceType=\"csn\"时,必传。<br/>LOCAL-网络实例带宽类型。<br>PEER_CLOUD-夸地域带宽云间互通<br/>PEER_EDGE-云边互通
        :type sub_service_type: str (optional)

        :param peer_region: 当subServiceType是PEER_CLOUD或PEER_EDGE时必传。表示对端地域。例如华北-北京传递\"bj\",华北保定传递\"bd\"
        :type peer_region: str (optional)

        :param resource_id:
            资源ID，对等连接ID或网关ID。当subServiceType=\"LOCAL\"时候，该resourceId=\"csnId:vpcId\"。
            当subServiceType=\"PEER_CLOUD\"时为csnId
        :type resource_id: str (required)

        :param direction: 限速方向: egress
        :type direction: str (required)

        :param cidr: 源网段CIDR,当前限流规则对当前设置的CIDR源网段生效。
        :type cidr: str (required)

        :param bandwidth: 带宽,Mbps,上限取决于具体网关的最大带宽。
        :type bandwidth: int (required)
        """
        super().__init__()
        self.client_token = client_token
        self.ip_version = ip_version
        self.name = name
        self.description = description
        self.service_type = service_type
        self.sub_service_type = sub_service_type
        self.peer_region = peer_region
        self.resource_id = resource_id
        self.direction = direction
        self.cidr = cidr
        self.bandwidth = bandwidth

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
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sub_service_type is not None:
            result['subServiceType'] = self.sub_service_type
        if self.peer_region is not None:
            result['peerRegion'] = self.peer_region
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.direction is not None:
            result['direction'] = self.direction
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateGatewayLimitRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('subServiceType') is not None:
            self.sub_service_type = m.get('subServiceType')
        if m.get('peerRegion') is not None:
            self.peer_region = m.get('peerRegion')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self
