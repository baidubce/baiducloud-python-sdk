"""
OperationRecordResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class OperationRecordResponse(BceResponse):
    """
    OperationRecordResponse
    """

    def __init__(self, name=None, operator=None, operate_time=None):
        """
        Initialize OperationRecordResponse instance.

        :param name: 操作名
        :type name: str (optional)

        :param operator: 操作人
        :type operator: str (optional)

        :param operate_time: 操作时间，符合BCE规范的日期格式
        :type operate_time: str (optional)
        """
        super().__init__()
        self.name = name
        self.operator = operator
        self.operate_time = operate_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
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
        if self.operator is not None:
            result['operator'] = self.operator
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OperationRecordResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        return self
