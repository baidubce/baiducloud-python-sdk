"""
Request entity for EcnetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EcnetRequest(AbstractModel):
    """
    Request entity for EcnetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, text, charset=None):
        """
        Initialize EcnetRequest request entity.

        :param charset: charset parameter
        :type charset: str (optional)

        :param text: 待纠错文本，输入限制550个汉字
        :type text: str (required)
        """
        super().__init__()
        self.charset = charset
        self.text = text

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
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EcnetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('charset') is not None:
            self.charset = m.get('charset')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self
