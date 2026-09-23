"""
Request entity for SimnetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SimnetRequest(AbstractModel):
    """
    Request entity for SimnetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, text_1, text_2, charset=None, model=None):
        """
        Initialize SimnetRequest request entity.

        :param charset: charset parameter
        :type charset: str (optional)

        :param text_1: 待比较文本1，最大512字节
        :type text_1: str (required)

        :param text_2: 待比较文本2，最大512字节
        :type text_2: str (required)

        :param model: model parameter
        :type model: str (optional)
        """
        super().__init__()
        self.charset = charset
        self.text_1 = text_1
        self.text_2 = text_2
        self.model = model

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
        if self.text_1 is not None:
            result['text_1'] = self.text_1
        if self.text_2 is not None:
            result['text_2'] = self.text_2
        if self.model is not None:
            result['model'] = self.model
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SimnetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('charset') is not None:
            self.charset = m.get('charset')
        if m.get('text_1') is not None:
            self.text_1 = m.get('text_1')
        if m.get('text_2') is not None:
            self.text_2 = m.get('text_2')
        if m.get('model') is not None:
            self.model = m.get('model')
        return self
