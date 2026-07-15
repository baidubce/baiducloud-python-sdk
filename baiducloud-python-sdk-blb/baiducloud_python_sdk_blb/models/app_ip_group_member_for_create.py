"""
AppIpGroupMemberForCreate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppIpGroupMemberForCreate(AbstractModel):
    """
    AppIpGroupMemberForCreate
    """

    def __init__(self, ip=None, port=None, weight=None, desc=None):
        """
        Initialize AppIpGroupMemberForCreate instance.

        :param ip: ipv4地址
        :type ip: str (optional)

        :param port: 端口号，取值范围1~65535
        :type port: int (optional)

        :param weight: 权重，取值范围0~100
        :type weight: int (optional)

        :param desc: 描述信息，最大支持200个字符
        :type desc: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.port = port
        self.weight = weight
        self.desc = desc

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
        if self.port is not None:
            result['port'] = self.port
        if self.weight is not None:
            result['weight'] = self.weight
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppIpGroupMemberForCreate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
