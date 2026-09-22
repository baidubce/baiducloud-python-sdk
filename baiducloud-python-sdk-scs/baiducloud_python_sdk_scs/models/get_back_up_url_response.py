"""
Request entity for GetBackUpUrlResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetBackUpUrlResponse(BceResponse):
    """
    GetBackUpUrlResponse
    """

    def __init__(self, url=None, url_expiration=None):
        """
        Initialize GetBackUpUrlResponse response.

        :param url: 下载地址。
        :type url: str (optional)

        :param url_expiration: 过期时间，单位秒。
        :type url_expiration: int (optional)
        """
        super().__init__()
        self.url = url
        self.url_expiration = url_expiration

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
        if self.url is not None:
            result['url'] = self.url
        if self.url_expiration is not None:
            result['urlExpiration'] = self.url_expiration
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetBackUpUrlResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('urlExpiration') is not None:
            self.url_expiration = m.get('urlExpiration')
        return self
