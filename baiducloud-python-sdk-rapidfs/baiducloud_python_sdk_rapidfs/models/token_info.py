"""
TokenInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TokenInfo(AbstractModel):
    """
    TokenInfo
    """

    def __init__(
        self,
        token_id=None,
        instance_id=None,
        token_value=None,
        token_refresh_interval_minutes=None,
        token_expire_time=None,
    ):
        """
        Initialize TokenInfo instance.

        :param token_id: 实例 Token 唯一 Id
        :type token_id: str (optional)

        :param instance_id: RapidFS 实例唯一 Id
        :type instance_id: str (optional)

        :param token_value: Token，仅在 DescribeToken 接口中返回
        :type token_value: str (optional)

        :param token_refresh_interval_minutes: Token更新周期，单位分钟，0 表示永不更新，最大值 43200 分钟
        :type token_refresh_interval_minutes: int (optional)

        :param token_expire_time: Token失效时刻
        :type token_expire_time: str (optional)
        """
        super().__init__()
        self.token_id = token_id
        self.instance_id = instance_id
        self.token_value = token_value
        self.token_refresh_interval_minutes = token_refresh_interval_minutes
        self.token_expire_time = token_expire_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.token_value is not None:
            result['tokenValue'] = self.token_value
        if self.token_refresh_interval_minutes is not None:
            result['tokenRefreshIntervalMinutes'] = self.token_refresh_interval_minutes
        if self.token_expire_time is not None:
            result['tokenExpireTime'] = self.token_expire_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TokenInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('tokenValue') is not None:
            self.token_value = m.get('tokenValue')
        if m.get('tokenRefreshIntervalMinutes') is not None:
            self.token_refresh_interval_minutes = m.get('tokenRefreshIntervalMinutes')
        if m.get('tokenExpireTime') is not None:
            self.token_expire_time = m.get('tokenExpireTime')
        return self
