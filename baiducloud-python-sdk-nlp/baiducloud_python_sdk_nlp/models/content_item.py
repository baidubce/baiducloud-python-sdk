"""
ContentItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.query_item import QueryItem


class ContentItem(AbstractModel):
    """
    ContentItem
    """

    def __init__(self, content=None, query_list=None):
        """
        Initialize ContentItem instance.

        :param content: 输入文本，每段文本不超过450个字符
        :type content: str (optional)

        :param query_list: 用户自定义的短语或问题列表，每段文本的短语或问题数量不超过5个
        :type query_list: List[QueryItem] (optional)
        """
        super().__init__()
        self.content = content
        self.query_list = query_list

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
        if self.content is not None:
            result['content'] = self.content
        if self.query_list is not None:
            result['query_list'] = [i.to_dict() for i in self.query_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ContentItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('query_list') is not None:
            self.query_list = [QueryItem().from_dict(i) for i in m.get('query_list')]
        return self
