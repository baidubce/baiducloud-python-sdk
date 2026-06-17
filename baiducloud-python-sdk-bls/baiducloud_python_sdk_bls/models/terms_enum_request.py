"""
Request entity for TermsEnumRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TermsEnumRequest(AbstractModel):
    """
    Request entity for TermsEnumRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, bls_field, string=None, size=None, index_filter=None):
        """
        Initialize TermsEnumRequest request entity.

        :param name: name parameter
        :type name: str (required)

        :param bls_field: 索引字段名称，不支持模糊匹配
        :type bls_field: str (required)

        :param string: 用于前缀匹配的字符串。比如 \"ki\" 会匹配以 ki 开头的 terms
        :type string: str (optional)

        :param size: 返回多少个terms 默认 10
        :type size: int (optional)

        :param index_filter: 限制从哪些文档里枚举 terms，语法同普通query DSL
        :type index_filter: object (optional)
        """
        super().__init__()
        self.name = name
        self.bls_field = bls_field
        self.string = string
        self.size = size
        self.index_filter = index_filter

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
        if self.bls_field is not None:
            result['field'] = self.bls_field
        if self.string is not None:
            result['string'] = self.string
        if self.size is not None:
            result['size'] = self.size
        if self.index_filter is not None:
            result['index_filter'] = self.index_filter
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TermsEnumRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('field') is not None:
            self.bls_field = m.get('field')
        if m.get('string') is not None:
            self.string = m.get('string')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('index_filter') is not None:
            self.index_filter = m.get('index_filter')
        return self
