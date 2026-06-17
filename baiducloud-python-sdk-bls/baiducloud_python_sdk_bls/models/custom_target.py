"""
CustomTarget information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.log_store import LogStore


class CustomTarget(AbstractModel):
    """
    CustomTarget
    """

    def __init__(self, query=None, start_time_offset_minute=None, end_time_offset_minute=None, object=None):
        """
        Initialize CustomTarget instance.

        :param query: 执行语句，必填
        :type query: str (optional)

        :param start_time_offset_minute: 查询开始时间偏移量，必填，取值范围: [-1440, 0)
        :type start_time_offset_minute: int (optional)

        :param end_time_offset_minute: 查询结束时间偏移量，必填，取值范围: (startTimeOffsetMinute, 0]
        :type end_time_offset_minute: int (optional)

        :param object: object attribute
        :type object: LogStore (optional)
        """
        super().__init__()
        self.query = query
        self.start_time_offset_minute = start_time_offset_minute
        self.end_time_offset_minute = end_time_offset_minute
        self.object = object

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
        if self.query is not None:
            result['query'] = self.query
        if self.start_time_offset_minute is not None:
            result['startTimeOffsetMinute'] = self.start_time_offset_minute
        if self.end_time_offset_minute is not None:
            result['endTimeOffsetMinute'] = self.end_time_offset_minute
        if self.object is not None:
            result['object'] = self.object.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CustomTarget

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('startTimeOffsetMinute') is not None:
            self.start_time_offset_minute = m.get('startTimeOffsetMinute')
        if m.get('endTimeOffsetMinute') is not None:
            self.end_time_offset_minute = m.get('endTimeOffsetMinute')
        if m.get('object') is not None:
            self.object = LogStore().from_dict(m.get('object'))
        return self
