"""
SampleProcessor information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.sample_filter import SampleFilter


class SampleProcessor(AbstractModel):
    """
    SampleProcessor
    """

    def __init__(self, name=None, enabled=None, filters=None, sample_rate=None):
        """
        Initialize SampleProcessor instance.

        :param name: 采样器名称，用户自定义
        :type name: str (optional)

        :param enabled: 是否启用当前采样器
        :type enabled: bool (optional)

        :param filters: 采样条件列表，多个采样条件之间是且关系
        :type filters: List[SampleFilter] (optional)

        :param sample_rate: 采样率，取值范围：[0, 1]
        :type sample_rate: float (optional)
        """
        super().__init__()
        self.name = name
        self.enabled = enabled
        self.filters = filters
        self.sample_rate = sample_rate

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SampleProcessor

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('filters') is not None:
            self.filters = [SampleFilter().from_dict(i) for i in m.get('filters')]
        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')
        return self
