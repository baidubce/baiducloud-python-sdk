"""
IndexField information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IndexField(AbstractModel):
    """
    IndexField
    """

    def __init__(self, type=None, case_sensitive=None, include_chinese=None, separators=None, dynamic_mapping=None):
        """
        Initialize IndexField instance.

        :param type: 字段索引类型
        :type type: str (optional)

        :param case_sensitive: 是否开启大小写敏感，默认false，不开启大小写敏感
        :type case_sensitive: bool (optional)

        :param include_chinese: 是否包含中文，默认为false，不包含中文
        :type include_chinese: bool (optional)

        :param separators: 分词符，不填使用默认分词符
        :type separators: str (optional)

        :param dynamic_mapping: 是否开启动态mapping
        :type dynamic_mapping: bool (optional)
        """
        super().__init__()
        self.type = type
        self.case_sensitive = case_sensitive
        self.include_chinese = include_chinese
        self.separators = separators
        self.dynamic_mapping = dynamic_mapping

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
        if self.type is not None:
            result['type'] = self.type
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.include_chinese is not None:
            result['includeChinese'] = self.include_chinese
        if self.separators is not None:
            result['separators'] = self.separators
        if self.dynamic_mapping is not None:
            result['dynamicMapping'] = self.dynamic_mapping
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IndexField

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('includeChinese') is not None:
            self.include_chinese = m.get('includeChinese')
        if m.get('separators') is not None:
            self.separators = m.get('separators')
        if m.get('dynamicMapping') is not None:
            self.dynamic_mapping = m.get('dynamicMapping')
        return self
