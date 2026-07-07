"""
Request entity for UserinfoEndpointResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class UserinfoEndpointResponse(BceResponse):
    """
    UserinfoEndpointResponse
    """

    def __init__(self, sub=None, username=None, display_name=None):
        """
        Initialize UserinfoEndpointResponse response.

        :param sub: 用户池用户 ID
        :type sub: str (optional)

        :param username: 用户名
        :type username: str (optional)

        :param display_name: 显示名称
        :type display_name: str (optional)
        """
        super().__init__()
        self.sub = sub
        self.username = username
        self.display_name = display_name

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
        if self.sub is not None:
            result['sub'] = self.sub
        if self.username is not None:
            result['username'] = self.username
        if self.display_name is not None:
            result['display_name'] = self.display_name
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserinfoEndpointResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sub') is not None:
            self.sub = m.get('sub')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')
        return self
