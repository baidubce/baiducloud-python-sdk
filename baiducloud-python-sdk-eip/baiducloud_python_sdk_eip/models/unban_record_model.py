"""
UnbanRecordModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UnbanRecordModel(AbstractModel):
    """
    UnbanRecordModel
    """

    def __init__(self, ip=None, protect_type=None, start_time=None, expect_end_time=None, status=None):
        """
        Initialize UnbanRecordModel instance.

        :param ip: IP地址，点分十进制表示
        :type ip: str (optional)

        :param protect_type: 防护类型，基础防护（0），TBSP增强防护（1）
        :type protect_type: int (optional)

        :param start_time: 封堵开始时间
        :type start_time: str (optional)

        :param expect_end_time: 预计解封时间
        :type expect_end_time: str (optional)

        :param status: 状态，解封（0），封禁中（1）
        :type status: int (optional)
        """
        super().__init__()
        self.ip = ip
        self.protect_type = protect_type
        self.start_time = start_time
        self.expect_end_time = expect_end_time
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
        if self.protect_type is not None:
            result['protectType'] = self.protect_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.expect_end_time is not None:
            result['expectEndTime'] = self.expect_end_time
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
        :rtype: UnbanRecordModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('protectType') is not None:
            self.protect_type = m.get('protectType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('expectEndTime') is not None:
            self.expect_end_time = m.get('expectEndTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
