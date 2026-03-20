"""
TbspIpModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspIpModel(AbstractModel):
    """
    TbspIpModel
    """

    def __init__(self, ip=None, status=None):
        """
        Initialize TbspIpModel instance.

        :param ip: DDoS增强防护包绑定防护对象IP地址
        :type ip: str (optional)

        :param status: DDoS增强防护包绑定防护对象运行状态
        :type status: str (optional)
        """
        super().__init__()
        self.ip = ip
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
        if self.ip is not None:
            result['ip'] = self.ip
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
        :rtype: TbspIpModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
