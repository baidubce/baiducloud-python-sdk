"""
InputModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InputModel(AbstractModel):
    """
    InputModel
    """

    def __init__(self, name=None, required=None, type=None, description=None, options=None, default=None):
        """
        Initialize InputModel instance.

        :param name: 参数名称
        :type name: str (optional)

        :param required: 是否必填
        :type required: bool (optional)

        :param type: 参数类型
        :type type: str (optional)

        :param description: 参数描述
        :type description: str (optional)

        :param options: 可选值列表
        :type options: List[object] (optional)

        :param default: 默认值
        :type default: object (optional)
        """
        super().__init__()
        self.name = name
        self.required = required
        self.type = type
        self.description = description
        self.options = options
        self.default = default

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
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        if self.options is not None:
            result['options'] = self.options
        if self.default is not None:
            result['default'] = self.default
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InputModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('default') is not None:
            self.default = m.get('default')
        return self
