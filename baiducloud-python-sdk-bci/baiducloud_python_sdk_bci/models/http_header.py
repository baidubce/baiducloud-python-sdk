"""
HTTPHeader information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HTTPHeader(AbstractModel):
    """
    HTTPHeader
    """

    def __init__(self, name=None, value=None):
        """
        Initialize HTTPHeader instance.

        :param name: http header name
        :type name: str (optional)

        :param value: http header value
        :type value: str (optional)
        """
        super().__init__()
        self.name = name
        self.value = value

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
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HTTPHeader

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
