"""
RdmaNicTopo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RdmaNicTopo(AbstractModel):
    """
    RdmaNicTopo
    """

    def __init__(self, rdma_ip=None, switch_name=None, switch_port=None, rdma_mac=None, rdma_gateway=None):
        """
        Initialize RdmaNicTopo instance.

        :param rdma_ip: RDMA IP地址
        :type rdma_ip: str (optional)

        :param switch_name: 交换机名称
        :type switch_name: str (optional)

        :param switch_port: 交换机端口
        :type switch_port: str (optional)

        :param rdma_mac: RDMA MAC地址
        :type rdma_mac: str (optional)

        :param rdma_gateway: RDMA网关
        :type rdma_gateway: str (optional)
        """
        super().__init__()
        self.rdma_ip = rdma_ip
        self.switch_name = switch_name
        self.switch_port = switch_port
        self.rdma_mac = rdma_mac
        self.rdma_gateway = rdma_gateway

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
        if self.rdma_ip is not None:
            result['rdmaIp'] = self.rdma_ip
        if self.switch_name is not None:
            result['switchName'] = self.switch_name
        if self.switch_port is not None:
            result['switchPort'] = self.switch_port
        if self.rdma_mac is not None:
            result['rdmaMac'] = self.rdma_mac
        if self.rdma_gateway is not None:
            result['rdmaGateway'] = self.rdma_gateway
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RdmaNicTopo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('rdmaIp') is not None:
            self.rdma_ip = m.get('rdmaIp')
        if m.get('switchName') is not None:
            self.switch_name = m.get('switchName')
        if m.get('switchPort') is not None:
            self.switch_port = m.get('switchPort')
        if m.get('rdmaMac') is not None:
            self.rdma_mac = m.get('rdmaMac')
        if m.get('rdmaGateway') is not None:
            self.rdma_gateway = m.get('rdmaGateway')
        return self
