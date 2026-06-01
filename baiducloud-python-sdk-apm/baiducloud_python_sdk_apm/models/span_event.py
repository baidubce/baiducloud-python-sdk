"""
SpanEvent information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SpanEvent(AbstractModel):
    """
    SpanEvent
    """

    def __init__(self, name=None, timestamp=None, attributes=None):
        """
        Initialize SpanEvent instance.

        :param name: 事件名称，若name=\"exception\"表示异常事件
        :type name: str (optional)

        :param timestamp: 事件发生的时间戳，单位：ns
        :type timestamp: int (optional)

        :param attributes: attributes attribute
        :type attributes: Dict[str, str] (optional)
        """
        super().__init__()
        self.name = name
        self.timestamp = timestamp
        self.attributes = attributes

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
        if self.name is not None:
            result['name'] = self.name
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.attributes is not None:
            result['attributes'] = self.attributes
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SpanEvent

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        return self
