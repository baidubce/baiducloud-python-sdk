"""
SampleConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.sample_processor import SampleProcessor


class SampleConfig(AbstractModel):
    """
    SampleConfig
    """

    def __init__(self, enabled=None, processors=None):
        """
        Initialize SampleConfig instance.

        :param enabled: 是否开启采样
        :type enabled: bool (optional)

        :param processors: 采样器列表
        :type processors: List[SampleProcessor] (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.processors = processors

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.processors is not None:
            result['processors'] = [i.to_dict() for i in self.processors]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SampleConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('processors') is not None:
            self.processors = [SampleProcessor().from_dict(i) for i in m.get('processors')]
        return self
