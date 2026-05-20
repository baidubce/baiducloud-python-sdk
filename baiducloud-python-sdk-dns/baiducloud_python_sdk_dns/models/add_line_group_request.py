"""
Request entity for AddLineGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddLineGroupRequest(AbstractModel):
    """
    Request entity for AddLineGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, lines, client_token=None):
        """
        Initialize AddLineGroupRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 线路组名称，长度不超过12个字符。
        :type name: str (required)

        :param lines: 解析线路。
        :type lines: List[str] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.lines = lines

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
        if self.name is not None:
            result['name'] = self.name
        if self.lines is not None:
            result['lines'] = self.lines
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddLineGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('lines') is not None:
            self.lines = m.get('lines')
        return self
