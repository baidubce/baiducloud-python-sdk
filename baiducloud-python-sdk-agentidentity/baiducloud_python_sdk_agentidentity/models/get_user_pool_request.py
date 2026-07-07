"""
Request entity for GetUserPoolRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetUserPoolRequest(AbstractModel):
    """
    Request entity for GetUserPoolRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id):
        """
        Initialize GetUserPoolRequest request entity.

        :param id: 用户池 ID
        :type id: str (required)
        """
        super().__init__()
        self.id = id

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
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetUserPoolRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
