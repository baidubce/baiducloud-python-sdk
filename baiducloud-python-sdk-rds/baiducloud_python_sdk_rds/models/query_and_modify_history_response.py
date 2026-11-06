"""
Request entity for QueryAndModifyHistoryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class QueryAndModifyHistoryResponse(BceResponse):
    """
    QueryAndModifyHistoryResponse
    """

    def __init__(self, name=None, before_value=None, after_value=None, status=None, update_time=None):
        """
        Initialize QueryAndModifyHistoryResponse response.

        :param name: 参数名
        :type name: str (optional)

        :param before_value: 修改前的值
        :type before_value: str (optional)

        :param after_value: 修改后的值
        :type after_value: str (optional)

        :param status: 修改状态：success：成功：pendingReboot：待重启
        :type status: str (optional)

        :param update_time: 修改时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.name = name
        self.before_value = before_value
        self.after_value = after_value
        self.status = status
        self.update_time = update_time

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
        if self.name is not None:
            result['name'] = self.name
        if self.before_value is not None:
            result['beforeValue'] = self.before_value
        if self.after_value is not None:
            result['afterValue'] = self.after_value
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryAndModifyHistoryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('beforeValue') is not None:
            self.before_value = m.get('beforeValue')
        if m.get('afterValue') is not None:
            self.after_value = m.get('afterValue')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
