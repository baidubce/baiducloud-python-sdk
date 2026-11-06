"""
SslState information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SslState(AbstractModel):
    """
    SslState
    """

    def __init__(self, instance_id=None, ssl_status=None, ssl_address=None, start_time=None, end_time=None):
        """
        Initialize SslState instance.

        :param instance_id: 实例 ID
        :type instance_id: str (optional)

        :param ssl_status: ssl状态, open: 开启，close: 关闭， 默认为close
        :type ssl_status: str (optional)

        :param ssl_address: 加密ssl地址 如:\"www.baidu.com\"
        :type ssl_address: str (optional)

        :param start_time: 开始日期
        :type start_time: str (optional)

        :param end_time: 结束日期
        :type end_time: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.ssl_status = ssl_status
        self.ssl_address = ssl_address
        self.start_time = start_time
        self.end_time = end_time

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.ssl_status is not None:
            result['sslStatus'] = self.ssl_status
        if self.ssl_address is not None:
            result['sslAddress'] = self.ssl_address
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SslState

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('sslStatus') is not None:
            self.ssl_status = m.get('sslStatus')
        if m.get('sslAddress') is not None:
            self.ssl_address = m.get('sslAddress')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
