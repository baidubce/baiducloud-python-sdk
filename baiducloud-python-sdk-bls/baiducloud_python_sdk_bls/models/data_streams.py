"""
DataStreams information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DataStreams(AbstractModel):
    """
    DataStreams
    """

    def __init__(self, name=None, backing_indices=None, timestamp_field=None):
        """
        Initialize DataStreams instance.

        :param name: 项目和日志集名称  default项目只显示名称了，非default项目为 项目名$日志集名称 的格式
        :type name: str (optional)

        :param backing_indices: 目前和name一样，只有单个元素
        :type backing_indices: List[str] (optional)

        :param timestamp_field: 时间字段, 取值为：@timestamp
        :type timestamp_field: str (optional)
        """
        super().__init__()
        self.name = name
        self.backing_indices = backing_indices
        self.timestamp_field = timestamp_field

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
        if self.backing_indices is not None:
            result['backing_indices'] = self.backing_indices
        if self.timestamp_field is not None:
            result['timestamp_field'] = self.timestamp_field
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DataStreams

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('backing_indices') is not None:
            self.backing_indices = m.get('backing_indices')
        if m.get('timestamp_field') is not None:
            self.timestamp_field = m.get('timestamp_field')
        return self
