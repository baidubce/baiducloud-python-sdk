"""
Request entity for MoveInEipsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MoveInEipsRequest(AbstractModel):
    """
    Request entity for MoveInEipsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, eips, client_token=None):
        """
        Initialize MoveInEipsRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param eips: 待移入的ip数组，包括IPv4 EIP和IPv6 EIP。
        :type eips: List[str] (required)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.eips = eips

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
        if self.eips is not None:
            result['eips'] = self.eips
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MoveInEipsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('eips') is not None:
            self.eips = m.get('eips')
        return self
