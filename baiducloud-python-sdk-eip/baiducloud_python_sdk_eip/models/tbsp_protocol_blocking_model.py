"""
TbspProtocolBlockingModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.tbsp_protocol_port_model import TbspProtocolPortModel


class TbspProtocolBlockingModel(AbstractModel):
    """
    TbspProtocolBlockingModel
    """

    def __init__(self, ip=None, protocol_port_list=None):
        """
        Initialize TbspProtocolBlockingModel instance.

        :param ip: DDoS增强防护包防护对象IP地址
        :type ip: str (optional)

        :param protocol_port_list: DDoS增强防护包协议封禁端口列表信息
        :type protocol_port_list: List[TbspProtocolPortModel] (optional)
        """
        super().__init__()
        self.ip = ip
        self.protocol_port_list = protocol_port_list

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.protocol_port_list is not None:
            result['protocolPortList'] = [i.to_dict() for i in self.protocol_port_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TbspProtocolBlockingModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('protocolPortList') is not None:
            self.protocol_port_list = [TbspProtocolPortModel().from_dict(i) for i in m.get('protocolPortList')]
        return self
