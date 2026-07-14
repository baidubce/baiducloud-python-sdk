"""
PolicyResource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.dimension import Dimension

from baiducloud_python_sdk_as.models.dimension import Dimension


class PolicyResource(AbstractModel):
    """
    PolicyResource
    """

    def __init__(self, identifiers=None, metric_dimensions=None):
        """
        Initialize PolicyResource instance.

        :param identifiers: 实例维度
        :type identifiers: List[Dimension] (optional)

        :param metric_dimensions: 指标维度
        :type metric_dimensions: List[Dimension] (optional)
        """
        super().__init__()
        self.identifiers = identifiers
        self.metric_dimensions = metric_dimensions

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
        if self.identifiers is not None:
            result['identifiers'] = [i.to_dict() for i in self.identifiers]
        if self.metric_dimensions is not None:
            result['metricDimensions'] = [i.to_dict() for i in self.metric_dimensions]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PolicyResource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('identifiers') is not None:
            self.identifiers = [Dimension().from_dict(i) for i in m.get('identifiers')]
        if m.get('metricDimensions') is not None:
            self.metric_dimensions = [Dimension().from_dict(i) for i in m.get('metricDimensions')]
        return self
