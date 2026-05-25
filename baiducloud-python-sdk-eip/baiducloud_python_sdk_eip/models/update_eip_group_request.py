"""
Request entity for UpdateEipGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateEipGroupRequest(AbstractModel):
    """
    Request entity for UpdateEipGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, name, client_token=None):
        """
        Initialize UpdateEipGroupRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 共享带宽名称
        :type name: str (required)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.name = name

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateEipGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
