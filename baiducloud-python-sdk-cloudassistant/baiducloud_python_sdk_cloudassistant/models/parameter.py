"""
Parameter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Parameter(AbstractModel):
    """
    Parameter
    """

    def __init__(self, name=None, desc=None, required=None, default_value=None):
        """
        Initialize Parameter instance.

        :param name: 参数名称
        :type name: str (optional)

        :param desc: 参数描述
        :type desc: str (optional)

        :param required: 是否必填
        :type required: bool (optional)

        :param default_value: 默认值
        :type default_value: str (optional)
        """
        super().__init__()
        self.name = name
        self.desc = desc
        self.required = required
        self.default_value = default_value

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
        if self.desc is not None:
            result['desc'] = self.desc
        if self.required is not None:
            result['required'] = self.required
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
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
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        return self
