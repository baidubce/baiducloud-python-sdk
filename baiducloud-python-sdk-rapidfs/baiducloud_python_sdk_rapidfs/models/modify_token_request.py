"""
Request entity for ModifyTokenRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyTokenRequest(AbstractModel):
    """
    Request entity for ModifyTokenRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, token_id, token_refresh_interval_minutes, client_token=None):
        """
        Initialize ModifyTokenRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: 所属 RapidFS 实例唯一 Id
        :type instance_id: str (required)

        :param token_id: Token id
        :type token_id: str (required)

        :param token_refresh_interval_minutes: Token更新周期，单位分钟，取值范围 [0, 43200(min)]；0 表示永不更新，Token 永久有效
        :type token_refresh_interval_minutes: int (required)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.token_id = token_id
        self.token_refresh_interval_minutes = token_refresh_interval_minutes

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
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        if self.token_refresh_interval_minutes is not None:
            result['tokenRefreshIntervalMinutes'] = self.token_refresh_interval_minutes
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyTokenRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        if m.get('tokenRefreshIntervalMinutes') is not None:
            self.token_refresh_interval_minutes = m.get('tokenRefreshIntervalMinutes')
        return self
