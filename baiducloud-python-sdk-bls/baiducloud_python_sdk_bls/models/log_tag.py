"""
LogTag information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogTag(AbstractModel):
    """
    LogTag
    """

    def __init__(self, k=None, v=None):
        """
        Initialize LogTag instance.

        :param k: 标签键
        :type k: str (optional)

        :param v: 标签值
        :type v: str (optional)
        """
        super().__init__()
        self.k = k
        self.v = v

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
        if self.k is not None:
            result['k'] = self.k
        if self.v is not None:
            result['v'] = self.v
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogTag

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('k') is not None:
            self.k = m.get('k')
        if m.get('v') is not None:
            self.v = m.get('v')
        return self
