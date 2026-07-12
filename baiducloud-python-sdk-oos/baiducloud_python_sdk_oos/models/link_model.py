"""
LinkModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LinkModel(AbstractModel):
    """
    LinkModel
    """

    def __init__(self, src=None, dst=None):
        """
        Initialize LinkModel instance.

        :param src: 上游 operator 的 name
        :type src: str (optional)

        :param dst: 下游 operator 的 name
        :type dst: str (optional)
        """
        super().__init__()
        self.src = src
        self.dst = dst

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
        if self.src is not None:
            result['src'] = self.src
        if self.dst is not None:
            result['dst'] = self.dst
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LinkModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('dst') is not None:
            self.dst = m.get('dst')
        return self
