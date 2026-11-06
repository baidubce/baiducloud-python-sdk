"""
Parameter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Parameter(AbstractModel):
    """
    Parameter
    """

    def __init__(self, name=None, value=None, apply_method=None, etag=None):
        """
        Initialize Parameter instance.

        :param name: 参数名
        :type name: str (optional)

        :param value: 参数取值
        :type value: str (optional)

        :param apply_method: apply_method attribute
        :type apply_method: str (optional)

        :param etag: 版本号
        :type etag: str (optional)
        """
        super().__init__()
        self.name = name
        self.value = value
        self.apply_method = apply_method
        self.etag = etag

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
        if self.apply_method is not None:
            result['applyMethod'] = self.apply_method
        if self.etag is not None:
            result['etag'] = self.etag
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Parameter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('applyMethod') is not None:
            self.apply_method = m.get('applyMethod')
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        return self
