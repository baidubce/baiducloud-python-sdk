"""
ModelField information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModelField(AbstractModel):
    """
    ModelField
    """

    def __init__(
        self,
        type=None,
        case_sensitive=None,
        include_chinese=None,
        separators=None,
        dynamic_mapping=None,
        searchable=None,
        aggregatable=None,
        metadata_field=None,
    ):
        """
        Initialize ModelField instance.

        :param type: 字段的类型，支持的类型有：bool、long、text、float、json
        :type type: str (optional)

        :param case_sensitive: 字段索引是否区分大小写，默认false，不区分
        :type case_sensitive: bool (optional)

        :param include_chinese: 字段索引是否包含中文，默认false，不包含
        :type include_chinese: bool (optional)

        :param separators: 字段索引自定义分隔符，不填使用默认分词符
        :type separators: str (optional)

        :param dynamic_mapping: 是否开启json动态索引，默认false，不开启
        :type dynamic_mapping: bool (optional)

        :param searchable: 该字段是否搜索
        :type searchable: bool (optional)

        :param aggregatable: 该字段是否可以聚合
        :type aggregatable: bool (optional)

        :param metadata_field: 该字段是否是元数据字段
        :type metadata_field: bool (optional)
        """
        super().__init__()
        self.type = type
        self.case_sensitive = case_sensitive
        self.include_chinese = include_chinese
        self.separators = separators
        self.dynamic_mapping = dynamic_mapping
        self.searchable = searchable
        self.aggregatable = aggregatable
        self.metadata_field = metadata_field

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
        if self.searchable is not None:
            result['searchable'] = self.searchable
        if self.aggregatable is not None:
            result['aggregatable'] = self.aggregatable
        if self.metadata_field is not None:
            result['metadata_field'] = self.metadata_field
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModelField

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
        if m.get('searchable') is not None:
            self.searchable = m.get('searchable')
        if m.get('aggregatable') is not None:
            self.aggregatable = m.get('aggregatable')
        if m.get('metadata_field') is not None:
            self.metadata_field = m.get('metadata_field')
        return self
