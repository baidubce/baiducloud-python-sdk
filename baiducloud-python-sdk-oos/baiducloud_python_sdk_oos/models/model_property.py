"""
ModelProperty information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.option import Option


class ModelProperty(AbstractModel):
    """
    ModelProperty
    """

    def __init__(
        self,
        name=None,
        required=None,
        type=None,
        label=None,
        description=None,
        multiple=None,
        options=None,
        select_options=None,
        default_value=None,
    ):
        """
        Initialize ModelProperty instance.

        :param name: 参数名称
        :type name: str (optional)

        :param required: 是否必填
        :type required: bool (optional)

        :param type: 参数类型
        :type type: str (optional)

        :param label: 参数显示名称
        :type label: str (optional)

        :param description: 参数描述
        :type description: str (optional)

        :param multiple: 可选项列表是否允许多选
        :type multiple: bool (optional)

        :param options: 可选项列表
        :type options: List[object] (optional)

        :param select_options: 新版可选项列表，目前仅系统操作符使用
        :type select_options: List[Option] (optional)

        :param default_value: 默认取值
        :type default_value: object (optional)
        """
        super().__init__()
        self.name = name
        self.required = required
        self.type = type
        self.label = label
        self.description = description
        self.multiple = multiple
        self.options = options
        self.select_options = select_options
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
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        if self.label is not None:
            result['label'] = self.label
        if self.description is not None:
            result['description'] = self.description
        if self.multiple is not None:
            result['multiple'] = self.multiple
        if self.options is not None:
            result['options'] = self.options
        if self.select_options is not None:
            result['selectOptions'] = [i.to_dict() for i in self.select_options]
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
        :rtype: ModelProperty

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
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('multiple') is not None:
            self.multiple = m.get('multiple')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('selectOptions') is not None:
            self.select_options = [Option().from_dict(i) for i in m.get('selectOptions')]
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        return self
