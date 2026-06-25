"""
LabelSelector information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LabelSelector(AbstractModel):
    """
    LabelSelector
    """

    def __init__(self, match_labels=None):
        """
        Initialize LabelSelector instance.

        :param match_labels: 标签键值对，如{\"k8s-app\":\"metrics-server\"}
        :type match_labels: Dict[str, str] (optional)
        """
        super().__init__()
        self.match_labels = match_labels

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
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LabelSelector

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        return self
