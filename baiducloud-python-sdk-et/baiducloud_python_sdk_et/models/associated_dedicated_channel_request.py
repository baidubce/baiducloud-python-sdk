"""
Request entity for AssociatedDedicatedChannelRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AssociatedDedicatedChannelRequest(AbstractModel):
    """
    Request entity for AssociatedDedicatedChannelRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_id, et_channel_id, extra_channel_id, client_token=None):
        """
        Initialize AssociatedDedicatedChannelRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param extra_channel_id: 被关联的专线通道ID
        :type extra_channel_id: str (required)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.extra_channel_id = extra_channel_id

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
        if self.extra_channel_id is not None:
            result['extraChannelId'] = self.extra_channel_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AssociatedDedicatedChannelRequest

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
        if m.get('extraChannelId') is not None:
            self.extra_channel_id = m.get('extraChannelId')
        return self
