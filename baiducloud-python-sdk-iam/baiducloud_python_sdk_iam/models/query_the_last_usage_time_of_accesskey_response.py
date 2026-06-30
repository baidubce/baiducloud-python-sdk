"""
Request entity for QueryTheLastUsageTimeOfAccesskeyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class QueryTheLastUsageTimeOfAccesskeyResponse(BceResponse):
    """
    QueryTheLastUsageTimeOfAccesskeyResponse
    """

    def __init__(self, access_key_id=None, last_used_time=None):
        """
        Initialize QueryTheLastUsageTimeOfAccesskeyResponse response.

        :param access_key_id: 访问密钥id
        :type access_key_id: str (optional)

        :param last_used_time: 访问密钥id的上次使用时间
        :type last_used_time: str (optional)
        """
        super().__init__()
        self.access_key_id = access_key_id
        self.last_used_time = last_used_time

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryTheLastUsageTimeOfAccesskeyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')
        return self
