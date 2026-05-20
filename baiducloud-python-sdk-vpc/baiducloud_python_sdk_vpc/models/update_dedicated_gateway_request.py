"""
Request entity for UpdateDedicatedGatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDedicatedGatewayRequest(AbstractModel):
    """
    Request entity for UpdateDedicatedGatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        et_gateway_id,
        client_token=None,
        name=None,
        speed=None,
        description=None,
        local_cidrs=None,
        enable_ipv6=None,
        ipv6_local_cidrs=None,
    ):
        """
        Initialize UpdateDedicatedGatewayRequest request entity.

        :param et_gateway_id: et_gateway_id parameter
        :type et_gateway_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 专线网关的名称，由大小写字母、数字以及-_ /.特殊字符组成，必须以字母开头，长度1-65
        :type name: str (optional)

        :param speed: 专线网关带宽的限速值，单位为Mbps。限制为2~100000之间的整数
        :type speed: int (optional)

        :param description: 专线网关的描述，不超过200字符
        :type description: str (optional)

        :param local_cidrs: 专线网关的IPv4云端网络，用户可以选本VPC网段或自定义一个或多个网段
        :type local_cidrs: List[str] (optional)

        :param enable_ipv6: IPv6功能是否开启，1是0否，IPv6为白名单功能
        :type enable_ipv6: int (optional)

        :param ipv6_local_cidrs: 专线网关的IPv6云端网络，用户可以选本VPC网段或自定义一个或多个IPv6网段
        :type ipv6_local_cidrs: List[str] (optional)
        """
        super().__init__()
        self.et_gateway_id = et_gateway_id
        self.client_token = client_token
        self.name = name
        self.speed = speed
        self.description = description
        self.local_cidrs = local_cidrs
        self.enable_ipv6 = enable_ipv6
        self.ipv6_local_cidrs = ipv6_local_cidrs

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
        if self.speed is not None:
            result['speed'] = self.speed
        if self.description is not None:
            result['description'] = self.description
        if self.local_cidrs is not None:
            result['localCidrs'] = self.local_cidrs
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.ipv6_local_cidrs is not None:
            result['ipv6LocalCidrs'] = self.ipv6_local_cidrs
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDedicatedGatewayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etGatewayId') is not None:
            self.et_gateway_id = m.get('etGatewayId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('localCidrs') is not None:
            self.local_cidrs = m.get('localCidrs')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('ipv6LocalCidrs') is not None:
            self.ipv6_local_cidrs = m.get('ipv6LocalCidrs')
        return self
