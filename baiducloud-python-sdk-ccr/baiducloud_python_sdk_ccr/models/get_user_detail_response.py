"""
Request entity for GetUserDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetUserDetailResponse(BceResponse):
    """
    GetUserDetailResponse
    """

    def __init__(self, name=None):
        """
        Initialize GetUserDetailResponse response.

        :param name: 用户名
        :type name: str (optional)
        """
        super().__init__()
        self.name = name

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
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetUserDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
