"""
ConsumerCredentialSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ConsumerCredentialSpec(AbstractModel):
    """
    ConsumerCredentialSpec
    """

    def __init__(
        self,
        name=None,
        generate_mode=None,
        value=None,
        in_header=None,
        in_query=None,
        key_names=None,
        description=None,
    ):
        """
        Initialize ConsumerCredentialSpec instance.

        :param name: 凭证名称
        :type name: str (optional)

        :param generate_mode: 生成模式
        :type generate_mode: str (optional)

        :param value: 凭证值
        :type value: str (optional)

        :param in_header: 是否放入请求头
        :type in_header: bool (optional)

        :param in_query: 是否放入查询参数
        :type in_query: bool (optional)

        :param key_names: 凭证键名
        :type key_names: List[str] (optional)

        :param description: 凭证描述
        :type description: str (optional)
        """
        super().__init__()
        self.name = name
        self.generate_mode = generate_mode
        self.value = value
        self.in_header = in_header
        self.in_query = in_query
        self.key_names = key_names
        self.description = description

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
        if self.generate_mode is not None:
            result['generateMode'] = self.generate_mode
        if self.value is not None:
            result['value'] = self.value
        if self.in_header is not None:
            result['inHeader'] = self.in_header
        if self.in_query is not None:
            result['inQuery'] = self.in_query
        if self.key_names is not None:
            result['keyNames'] = self.key_names
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConsumerCredentialSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateMode') is not None:
            self.generate_mode = m.get('generateMode')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('inHeader') is not None:
            self.in_header = m.get('inHeader')
        if m.get('inQuery') is not None:
            self.in_query = m.get('inQuery')
        if m.get('keyNames') is not None:
            self.key_names = m.get('keyNames')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
