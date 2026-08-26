"""
MetricCatalog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.metric import Metric


class MetricCatalog(AbstractModel):
    """
    MetricCatalog
    """

    def __init__(self, name=None, label=None, catalogs=None, metrics=None):
        """
        Initialize MetricCatalog instance.

        :param name: 指标目录名称
        :type name: str (optional)

        :param label: 指标目录显示名称，根据locale返回中文或英文名称
        :type label: str (optional)

        :param catalogs: 当前目录下的子目录列表，结构与catalogs相同
        :type catalogs: List[MetricCatalog] (optional)

        :param metrics: 当前目录下的指标列表
        :type metrics: List[Metric] (optional)
        """
        super().__init__()
        self.name = name
        self.label = label
        self.catalogs = catalogs
        self.metrics = metrics

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
        if self.label is not None:
            result['label'] = self.label
        if self.catalogs is not None:
            result['catalogs'] = [i.to_dict() for i in self.catalogs]
        if self.metrics is not None:
            result['metrics'] = [i.to_dict() for i in self.metrics]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MetricCatalog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('catalogs') is not None:
            self.catalogs = [MetricCatalog().from_dict(i) for i in m.get('catalogs')]
        if m.get('metrics') is not None:
            self.metrics = [Metric().from_dict(i) for i in m.get('metrics')]
        return self
