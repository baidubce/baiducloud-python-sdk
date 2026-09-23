"""
Request entity for TopicRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TopicRequest(AbstractModel):
    """
    Request entity for TopicRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, title, content, charset=None):
        """
        Initialize TopicRequest request entity.

        :param charset: charset parameter
        :type charset: str (optional)

        :param title: 文章标题，最大80字节
        :type title: str (required)

        :param content: 文章内容，最大65535字节
        :type content: str (required)
        """
        super().__init__()
        self.charset = charset
        self.title = title
        self.content = content

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
        if self.title is not None:
            result['title'] = self.title
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TopicRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('charset') is not None:
            self.charset = m.get('charset')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self
