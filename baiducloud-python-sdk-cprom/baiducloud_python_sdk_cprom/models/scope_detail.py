"""
ScopeDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ScopeDetail(AbstractModel):
    """
    ScopeDetail
    """

    def __init__(self, scope_name=None, humanization=None, doc_link=None):
        """
        Initialize ScopeDetail instance.

        :param scope_name: 云产品英文名称，如 `BCE_BCC`
        :type scope_name: str (optional)

        :param humanization: 云产品说明
        :type humanization: str (optional)

        :param doc_link: BCM 文档链接
        :type doc_link: str (optional)
        """
        super().__init__()
        self.scope_name = scope_name
        self.humanization = humanization
        self.doc_link = doc_link

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
        if self.scope_name is not None:
            result['scopeName'] = self.scope_name
        if self.humanization is not None:
            result['humanization'] = self.humanization
        if self.doc_link is not None:
            result['docLink'] = self.doc_link
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ScopeDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scopeName') is not None:
            self.scope_name = m.get('scopeName')
        if m.get('humanization') is not None:
            self.humanization = m.get('humanization')
        if m.get('docLink') is not None:
            self.doc_link = m.get('docLink')
        return self
