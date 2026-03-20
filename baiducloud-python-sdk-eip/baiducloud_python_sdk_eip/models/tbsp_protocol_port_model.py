"""
TbspProtocolPortModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspProtocolPortModel(AbstractModel):
    """
    TbspProtocolPortModel
    """

    def __init__(self, type=None, port_begin=None, port_end=None):
        """
        Initialize TbspProtocolPortModel instance.

        :param type: DDoS增强防护包封禁协议类型，包含icmp、tcp和udp
        :type type: str (optional)

        :param port_begin: DDoS增强防护包协议封禁端口起始值
        :type port_begin: int (optional)

        :param port_end: DDoS增强防护包协议封禁端口终止值
        :type port_end: int (optional)
        """
        super().__init__()
        self.type = type
        self.port_begin = port_begin
        self.port_end = port_end

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
        if self.type is not None:
            result['type'] = self.type
        if self.port_begin is not None:
            result['portBegin'] = self.port_begin
        if self.port_end is not None:
            result['portEnd'] = self.port_end
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TbspProtocolPortModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('portBegin') is not None:
            self.port_begin = m.get('portBegin')
        if m.get('portEnd') is not None:
            self.port_end = m.get('portEnd')
        return self
