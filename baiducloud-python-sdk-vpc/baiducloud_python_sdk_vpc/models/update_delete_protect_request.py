"""
Request entity for UpdateDeleteProtectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDeleteProtectRequest(AbstractModel):
    """
    Request entity for UpdateDeleteProtectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, gateway_id, delete_protect, client_token=None):
        """
        Initialize UpdateDeleteProtectRequest request entity.

        :param gateway_id: gateway_id parameter
        :type gateway_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param delete_protect: 是否开启释放保护
        :type delete_protect: int (required)
        """
        super().__init__()
        self.gateway_id = gateway_id
        self.client_token = client_token
        self.delete_protect = delete_protect

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
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDeleteProtectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
