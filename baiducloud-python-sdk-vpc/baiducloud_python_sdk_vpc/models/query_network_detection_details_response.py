"""
Request entity for QueryNetworkDetectionDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class QueryNetworkDetectionDetailsResponse(BceResponse):
    """
    QueryNetworkDetectionDetailsResponse
    """

    def __init__(
        self,
        probe_id=None,
        description=None,
        dest_ip=None,
        dest_port=None,
        frequency=None,
        name=None,
        payload=None,
        protocol=None,
        source_ips=None,
        status=None,
        subnet_id=None,
        vpc_id=None,
    ):
        """
        Initialize QueryNetworkDetectionDetailsResponse response.

        :param probe_id: 探测ID
        :type probe_id: str (optional)

        :param description: 探测描述
        :type description: str (optional)

        :param dest_ip: 目的地址
        :type dest_ip: str (optional)

        :param dest_port: 目的端口
        :type dest_port: str (optional)

        :param frequency: 探测频率
        :type frequency: int (optional)

        :param name: 探测名称
        :type name: str (optional)

        :param payload: 探测内容实体
        :type payload: str (optional)

        :param protocol: 探测类型，TCP、UDP、ICMP、DNS
        :type protocol: str (optional)

        :param source_ips: 探测源地址
        :type source_ips: List[str] (optional)

        :param status: 状态，active可用
        :type status: str (optional)

        :param subnet_id: 所属子网ID
        :type subnet_id: str (optional)

        :param vpc_id: 所属VPC ID
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.probe_id = probe_id
        self.description = description
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.frequency = frequency
        self.name = name
        self.payload = payload
        self.protocol = protocol
        self.source_ips = source_ips
        self.status = status
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id

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
        if self.probe_id is not None:
            result['probeId'] = self.probe_id
        if self.description is not None:
            result['description'] = self.description
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.dest_port is not None:
            result['destPort'] = self.dest_port
        if self.frequency is not None:
            result['frequency'] = self.frequency
        if self.name is not None:
            result['name'] = self.name
        if self.payload is not None:
            result['payload'] = self.payload
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.source_ips is not None:
            result['sourceIps'] = self.source_ips
        if self.status is not None:
            result['status'] = self.status
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryNetworkDetectionDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('probeId') is not None:
            self.probe_id = m.get('probeId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('destPort') is not None:
            self.dest_port = m.get('destPort')
        if m.get('frequency') is not None:
            self.frequency = m.get('frequency')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('sourceIps') is not None:
            self.source_ips = m.get('sourceIps')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
