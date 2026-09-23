"""
Request entity for NewsSummaryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NewsSummaryRequest(AbstractModel):
    """
    Request entity for NewsSummaryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, content, max_summary_len, charset=None, title=None):
        """
        Initialize NewsSummaryRequest request entity.

        :param charset: charset parameter
        :type charset: str (optional)

        :param title: title parameter
        :type title: str (optional)

        :param content: content parameter
        :type content: str (required)

        :param max_summary_len: max_summary_len parameter
        :type max_summary_len: int (required)
        """
        super().__init__()
        self.charset = charset
        self.title = title
        self.content = content
        self.max_summary_len = max_summary_len

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
        if self.max_summary_len is not None:
            result['max_summary_len'] = self.max_summary_len
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NewsSummaryRequest

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
        if m.get('max_summary_len') is not None:
            self.max_summary_len = m.get('max_summary_len')
        return self
