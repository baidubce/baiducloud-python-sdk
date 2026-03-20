"""
TbspAttackRecordModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspAttackRecordModel(AbstractModel):
    """
    TbspAttackRecordModel
    """

    def __init__(self, ip=None, start_time=None):
        """
        Initialize TbspAttackRecordModel instance.

        :param ip: DDoS增强防护包被攻击的IP地址
        :type ip: str (optional)

        :param start_time: 攻击开始时间
        :type start_time: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.start_time = start_time

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TbspAttackRecordModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self
