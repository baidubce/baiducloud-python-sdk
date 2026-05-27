"""
Request entity for CreateProbeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateProbeRequest(AbstractModel):
    """
    Request entity for CreateProbeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        vpc_id,
        subnet_id,
        protocol,
        frequency,
        source_ips,
        dest_ip,
        client_token=None,
        description=None,
        source_ip_num=None,
        dest_port=None,
        payload=None,
    ):
        """
        Initialize CreateProbeRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 网络探测名称，长度不超过65个字符，可由数字、字符、下划线组成
        :type name: str (required)

        :param description: 网络探测描述，不超过200字符
        :type description: str (optional)

        :param vpc_id: 网络探测所属VPC ID
        :type vpc_id: str (required)

        :param subnet_id: 网络探测所属子网ID
        :type subnet_id: str (required)

        :param protocol: 探测类型，目前支持ICMP、TCP、UDP、DNS
        :type protocol: str (required)

        :param frequency: 探测频率取值为10、20、30
        :type frequency: int (required)

        :param source_ips: 探测源IP列表，可以不指定列表为空，该情况sourceIpNum就必须取值
        :type source_ips: List[str] (required)

        :param source_ip_num: 自动分配的探测源IP个数
        :type source_ip_num: int (optional)

        :param dest_ip: 探测目的IP
        :type dest_ip: str (required)

        :param dest_port: 探测目的端口，TCP、UDP和DNS类型的需要
        :type dest_port: int (optional)

        :param payload: UDP类型的探测字符串和DNS类型的探测域名
        :type payload: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.protocol = protocol
        self.frequency = frequency
        self.source_ips = source_ips
        self.source_ip_num = source_ip_num
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.payload = payload

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.frequency is not None:
            result['frequency'] = self.frequency
        if self.source_ips is not None:
            result['sourceIps'] = self.source_ips
        if self.source_ip_num is not None:
            result['sourceIpNum'] = self.source_ip_num
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.dest_port is not None:
            result['destPort'] = self.dest_port
        if self.payload is not None:
            result['payload'] = self.payload
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateProbeRequest

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
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('frequency') is not None:
            self.frequency = m.get('frequency')
        if m.get('sourceIps') is not None:
            self.source_ips = m.get('sourceIps')
        if m.get('sourceIpNum') is not None:
            self.source_ip_num = m.get('sourceIpNum')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('destPort') is not None:
            self.dest_port = m.get('destPort')
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        return self
