"""
Request entity for DeleteInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteInstanceRequest(AbstractModel):
    """
    Request entity for DeleteInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, client_token=None, token=None):
        """
        Initialize DeleteInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: 待释放的 RapidFS 实例 ID
        :type instance_id: str (required)

        :param token: token parameter
        :type token: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.token = token

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self
