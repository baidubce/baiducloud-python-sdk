"""
Request entity for TxtMonetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_nlp.models.content_item import ContentItem


class TxtMonetRequest(AbstractModel):
    """
    Request entity for TxtMonetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, content_list, charset=None):
        """
        Initialize TxtMonetRequest request entity.

        :param charset: charset parameter
        :type charset: str (optional)

        :param content_list: 输入的文本列表，支持不超过2段的文本进行批量提取
        :type content_list: List[ContentItem] (required)
        """
        super().__init__()
        self.charset = charset
        self.content_list = content_list

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
        if self.content_list is not None:
            result['content_list'] = [i.to_dict() for i in self.content_list]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TxtMonetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('charset') is not None:
            self.charset = m.get('charset')
        if m.get('content_list') is not None:
            self.content_list = [ContentItem().from_dict(i) for i in m.get('content_list')]
        return self
