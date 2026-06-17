"""
Request entity for CreateIndexRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.index_field import IndexField


class CreateIndexRequest(AbstractModel):
    """
    Request entity for CreateIndexRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        log_store_name,
        project=None,
        fulltext=None,
        case_sensitive=None,
        include_chinese=None,
        separators=None,
        fields=None,
    ):
        """
        Initialize CreateIndexRequest request entity.

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (required)

        :param project: project parameter
        :type project: str (optional)

        :param fulltext: 是否开启全文索引，true 表示开启
        :type fulltext: bool (optional)

        :param case_sensitive: 全文索引是否开启大小写敏感，默认false，不开启大小写敏感
        :type case_sensitive: bool (optional)

        :param include_chinese: 是否包含中文，默认为false，不包含中文
        :type include_chinese: bool (optional)

        :param separators: 全文分词符，不填使用默认分词符
        :type separators: str (optional)

        :param fields: 字段索引包含的字段名称及类型定义
        :type fields: Dict[str, IndexField] (optional)
        """
        super().__init__()
        self.log_store_name = log_store_name
        self.project = project
        self.fulltext = fulltext
        self.case_sensitive = case_sensitive
        self.include_chinese = include_chinese
        self.separators = separators
        self.fields = fields

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.fulltext is not None:
            result['fulltext'] = self.fulltext
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.include_chinese is not None:
            result['includeChinese'] = self.include_chinese
        if self.separators is not None:
            result['separators'] = self.separators
        if self.fields is not None:
            result['fields'] = {k: v.to_dict() for k, v in self.fields.items()}
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIndexRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('fulltext') is not None:
            self.fulltext = m.get('fulltext')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('includeChinese') is not None:
            self.include_chinese = m.get('includeChinese')
        if m.get('separators') is not None:
            self.separators = m.get('separators')
        if m.get('fields') is not None:
            self.fields = {k: IndexField().from_dict(v) for k, v in m.get('fields').items()}
        return self
