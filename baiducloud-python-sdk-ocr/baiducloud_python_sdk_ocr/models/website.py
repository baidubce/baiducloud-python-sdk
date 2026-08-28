"""
Website information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Website(AbstractModel):
    """
    Website
    """

    def __init__(self, name=None, url=None):
        """
        Initialize Website instance.

        :param name: 网站名称
        :type name: str (optional)

        :param url: 网站地址
        :type url: str (optional)
        """
        super().__init__()
        self.name = name
        self.url = url

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
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Website

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self
