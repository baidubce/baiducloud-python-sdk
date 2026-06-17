"""
Request entity for DescribeIndexResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.index_field import IndexField


class DescribeIndexResponse(BceResponse):
    """
    DescribeIndexResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        fulltext=None,
        fields=None,
        case_sensitive=None,
        include_chinese=None,
        separators=None,
    ):
        """
        Initialize DescribeIndexResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)

        :param fulltext: 是否开启全文索引，true 表示开启
        :type fulltext: bool (optional)

        :param fields: 字段索引的字段名称和类型信息
        :type fields: Dict[str, IndexField] (optional)

        :param case_sensitive: 全文索引是否开启大小写敏感，true表示开启大小写敏感
        :type case_sensitive: bool (optional)

        :param include_chinese: 是否包含中文，true表示包含中文
        :type include_chinese: bool (optional)

        :param separators: 全文分词符
        :type separators: str (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.fulltext = fulltext
        self.fields = fields
        self.case_sensitive = case_sensitive
        self.include_chinese = include_chinese
        self.separators = separators

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.fulltext is not None:
            result['fulltext'] = self.fulltext
        if self.fields is not None:
            result['fields'] = [i.to_dict() for i in self.fields]
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.include_chinese is not None:
            result['includeChinese'] = self.include_chinese
        if self.separators is not None:
            result['separators'] = self.separators
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeIndexResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('fulltext') is not None:
            self.fulltext = m.get('fulltext')
        if m.get('fields') is not None:
            self.fields = [IndexField().from_dict(i) for i in m.get('fields')]
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('includeChinese') is not None:
            self.include_chinese = m.get('includeChinese')
        if m.get('separators') is not None:
            self.separators = m.get('separators')
        return self
