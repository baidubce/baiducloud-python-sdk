"""
VpcEndpoint information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VpcEndpoint(AbstractModel):
    """
    VpcEndpoint
    """

    def __init__(
        self,
        vpc_endpoint_id=None,
        vpc_id=None,
        protocol=None,
        backend_ip=None,
        backend_port=None,
        endpoint_ip=None,
        endpoint_port=None,
        name=None,
        description=None,
        type=None,
        status=None,
    ):
        """
        Initialize VpcEndpoint instance.

        :param vpc_endpoint_id: VPC Endpoint ID
        :type vpc_endpoint_id: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)

        :param protocol: 协议
        :type protocol: str (optional)

        :param backend_ip: 后端 IP
        :type backend_ip: str (optional)

        :param backend_port: 后端端口
        :type backend_port: str (optional)

        :param endpoint_ip: Endpoint IP
        :type endpoint_ip: str (optional)

        :param endpoint_port: Endpoint 端口
        :type endpoint_port: str (optional)

        :param name: Endpoint 名称
        :type name: str (optional)

        :param description: Endpoint 描述
        :type description: str (optional)

        :param type: Endpoint 类型
        :type type: str (optional)

        :param status: Endpoint 状态
        :type status: str (optional)
        """
        super().__init__()
        self.vpc_endpoint_id = vpc_endpoint_id
        self.vpc_id = vpc_id
        self.protocol = protocol
        self.backend_ip = backend_ip
        self.backend_port = backend_port
        self.endpoint_ip = endpoint_ip
        self.endpoint_port = endpoint_port
        self.name = name
        self.description = description
        self.type = type
        self.status = status

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
        if self.vpc_endpoint_id is not None:
            result['vpcEndpointId'] = self.vpc_endpoint_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.backend_ip is not None:
            result['backendIp'] = self.backend_ip
        if self.backend_port is not None:
            result['backendPort'] = self.backend_port
        if self.endpoint_ip is not None:
            result['endpointIp'] = self.endpoint_ip
        if self.endpoint_port is not None:
            result['endpointPort'] = self.endpoint_port
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VpcEndpoint

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcEndpointId') is not None:
            self.vpc_endpoint_id = m.get('vpcEndpointId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('backendIp') is not None:
            self.backend_ip = m.get('backendIp')
        if m.get('backendPort') is not None:
            self.backend_port = m.get('backendPort')
        if m.get('endpointIp') is not None:
            self.endpoint_ip = m.get('endpointIp')
        if m.get('endpointPort') is not None:
            self.endpoint_port = m.get('endpointPort')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
