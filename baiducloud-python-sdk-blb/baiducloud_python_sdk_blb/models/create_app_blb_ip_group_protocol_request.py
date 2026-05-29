"""
Request entity for CreateAppBlbIpGroupProtocolRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAppBlbIpGroupProtocolRequest(AbstractModel):
    """
    Request entity for CreateAppBlbIpGroupProtocolRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        blb_id,
        ip_group_id,
        type,
        client_token=None,
        health_check=None,
        health_check_port=None,
        health_check_url_path=None,
        health_check_timeout_in_second=None,
        health_check_interval_in_second=None,
        health_check_down_retry=None,
        health_check_up_retry=None,
        health_check_normal_status=None,
        health_check_host=None,
        udp_health_check_string=None,
    ):
        """
        Initialize CreateAppBlbIpGroupProtocolRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_group_id: 所属IP组的标识符
        :type ip_group_id: str (required)

        :param type: IP组开放协议类型，\"TCP\"/\"HTTP\"/\"HTTPS\"/\"UDP\"
        :type type: str (required)

        :param health_check: health_check parameter
        :type health_check: str (optional)

        :param health_check_port: 健康检查端口，IP组协议为HTTP协议时必传
        :type health_check_port: int (optional)

        :param health_check_url_path: 健康检查路径，默认/，当健康检查协议为\"HTTP\"时生效
        :type health_check_url_path: str (optional)

        :param health_check_timeout_in_second: 健康检查超时（单位：秒），默认为3，需为1-60间的整数
        :type health_check_timeout_in_second: int (optional)

        :param health_check_interval_in_second: 健康检查间隔（单位：秒），默认为3，需为1-10间的整数
        :type health_check_interval_in_second: int (optional)

        :param health_check_down_retry: 不健康阈值，即连续多少次健康检查失败后，屏蔽该后端服务器。默认为3，需为2-5间的整数
        :type health_check_down_retry: int (optional)

        :param health_check_up_retry: 健康阈值，即连续多少次健康检查成功后，重新将该后端服务器置为可用。默认为3，需为2-5间的整数
        :type health_check_up_retry: int (optional)

        :param health_check_normal_status: 健康检查正常时的HTTP状态码，支持5类状态码的组合，例如\"http_1xx
        :type health_check_normal_status: str (optional)

        :param health_check_host: health_check_host parameter
        :type health_check_host: str (optional)

        :param udp_health_check_string: UDP健康检查字符串，当健康检查协议为\"UDP\"时必传
        :type udp_health_check_string: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.ip_group_id = ip_group_id
        self.type = type
        self.health_check = health_check
        self.health_check_port = health_check_port
        self.health_check_url_path = health_check_url_path
        self.health_check_timeout_in_second = health_check_timeout_in_second
        self.health_check_interval_in_second = health_check_interval_in_second
        self.health_check_down_retry = health_check_down_retry
        self.health_check_up_retry = health_check_up_retry
        self.health_check_normal_status = health_check_normal_status
        self.health_check_host = health_check_host
        self.udp_health_check_string = udp_health_check_string

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
        if self.ip_group_id is not None:
            result['ipGroupId'] = self.ip_group_id
        if self.type is not None:
            result['type'] = self.type
        if self.health_check is not None:
            result['healthCheck'] = self.health_check
        if self.health_check_port is not None:
            result['healthCheckPort'] = self.health_check_port
        if self.health_check_url_path is not None:
            result['healthCheckUrlPath'] = self.health_check_url_path
        if self.health_check_timeout_in_second is not None:
            result['healthCheckTimeoutInSecond'] = self.health_check_timeout_in_second
        if self.health_check_interval_in_second is not None:
            result['healthCheckIntervalInSecond'] = self.health_check_interval_in_second
        if self.health_check_down_retry is not None:
            result['healthCheckDownRetry'] = self.health_check_down_retry
        if self.health_check_up_retry is not None:
            result['healthCheckUpRetry'] = self.health_check_up_retry
        if self.health_check_normal_status is not None:
            result['healthCheckNormalStatus'] = self.health_check_normal_status
        if self.health_check_host is not None:
            result['healthCheckHost'] = self.health_check_host
        if self.udp_health_check_string is not None:
            result['udpHealthCheckString'] = self.udp_health_check_string
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAppBlbIpGroupProtocolRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('healthCheck') is not None:
            self.health_check = m.get('healthCheck')
        if m.get('healthCheckPort') is not None:
            self.health_check_port = m.get('healthCheckPort')
        if m.get('healthCheckUrlPath') is not None:
            self.health_check_url_path = m.get('healthCheckUrlPath')
        if m.get('healthCheckTimeoutInSecond') is not None:
            self.health_check_timeout_in_second = m.get('healthCheckTimeoutInSecond')
        if m.get('healthCheckIntervalInSecond') is not None:
            self.health_check_interval_in_second = m.get('healthCheckIntervalInSecond')
        if m.get('healthCheckDownRetry') is not None:
            self.health_check_down_retry = m.get('healthCheckDownRetry')
        if m.get('healthCheckUpRetry') is not None:
            self.health_check_up_retry = m.get('healthCheckUpRetry')
        if m.get('healthCheckNormalStatus') is not None:
            self.health_check_normal_status = m.get('healthCheckNormalStatus')
        if m.get('healthCheckHost') is not None:
            self.health_check_host = m.get('healthCheckHost')
        if m.get('udpHealthCheckString') is not None:
            self.udp_health_check_string = m.get('udpHealthCheckString')
        return self
