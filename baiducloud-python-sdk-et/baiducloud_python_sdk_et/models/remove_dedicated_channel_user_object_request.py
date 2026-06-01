"""
Request entity for RemoveDedicatedChannelUserObjectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoveDedicatedChannelUserObjectRequest(AbstractModel):
    """
    Request entity for RemoveDedicatedChannelUserObjectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_id, et_channel_id, authorized_users, client_token=None):
        """
        Initialize RemoveDedicatedChannelUserObjectRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param authorized_users: 分配对象
        :type authorized_users: List[str] (required)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.authorized_users = authorized_users

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
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoveDedicatedChannelUserObjectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('etChannelId') is not None:
            self.et_channel_id = m.get('etChannelId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        return self
