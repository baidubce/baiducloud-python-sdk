"""
Request entity for CreateDedicatedGatewayHealthCheckRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDedicatedGatewayHealthCheckRequest(AbstractModel):
    """
    Request entity for CreateDedicatedGatewayHealthCheckRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        et_gateway_id,
        health_check_interval,
        health_threshold,
        unhealth_threshold,
        client_token=None,
        health_check_source_ip=None,
        health_check_type=None,
        auto_generate_route_rule=None,
    ):
        """
        Initialize CreateDedicatedGatewayHealthCheckRequest request entity.

        :param et_gateway_id: et_gateway_id parameter
        :type et_gateway_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param health_check_source_ip: 若不传该参数，系统会自动分配一个IP
        :type health_check_source_ip: str (optional)

        :param health_check_type: 参数可取值为\"ICMP\"，默认为\"ICMP\"
        :type health_check_type: str (optional)

        :param health_check_interval: 健康检查的间隔，1-60之间的整数，单位s
        :type health_check_interval: int (required)

        :param health_threshold: 健康检查阈值，2-5之间的整数
        :type health_threshold: int (required)

        :param unhealth_threshold: 不健康检查阈值，2-5之间的整数
        :type unhealth_threshold: int (required)

        :param auto_generate_route_rule: 是否自动生成探测路由，默认开启。如需关闭，选择false。
        :type auto_generate_route_rule: bool (optional)
        """
        super().__init__()
        self.et_gateway_id = et_gateway_id
        self.client_token = client_token
        self.health_check_source_ip = health_check_source_ip
        self.health_check_type = health_check_type
        self.health_check_interval = health_check_interval
        self.health_threshold = health_threshold
        self.unhealth_threshold = unhealth_threshold
        self.auto_generate_route_rule = auto_generate_route_rule

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
        if self.health_check_source_ip is not None:
            result['healthCheckSourceIp'] = self.health_check_source_ip
        if self.health_check_type is not None:
            result['healthCheckType'] = self.health_check_type
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.health_threshold is not None:
            result['healthThreshold'] = self.health_threshold
        if self.unhealth_threshold is not None:
            result['unhealthThreshold'] = self.unhealth_threshold
        if self.auto_generate_route_rule is not None:
            result['autoGenerateRouteRule'] = self.auto_generate_route_rule
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDedicatedGatewayHealthCheckRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etGatewayId') is not None:
            self.et_gateway_id = m.get('etGatewayId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('healthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('healthCheckSourceIp')
        if m.get('healthCheckType') is not None:
            self.health_check_type = m.get('healthCheckType')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('healthThreshold') is not None:
            self.health_threshold = m.get('healthThreshold')
        if m.get('unhealthThreshold') is not None:
            self.unhealth_threshold = m.get('unhealthThreshold')
        if m.get('autoGenerateRouteRule') is not None:
            self.auto_generate_route_rule = m.get('autoGenerateRouteRule')
        return self
