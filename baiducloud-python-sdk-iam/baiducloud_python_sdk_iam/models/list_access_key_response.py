"""
Request entity for ListAccessKeyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.access_key import AccessKey


class ListAccessKeyResponse(BceResponse):
    """
    ListAccessKeyResponse
    """

    def __init__(self, access_keys=None):
        """
        Initialize ListAccessKeyResponse response.

        :param access_keys: 用户访问密钥列表
        :type access_keys: List[AccessKey] (optional)
        """
        super().__init__()
        self.access_keys = access_keys

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
        if self.access_keys is not None:
            result['accessKeys'] = [i.to_dict() for i in self.access_keys]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListAccessKeyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessKeys') is not None:
            self.access_keys = [AccessKey().from_dict(i) for i in m.get('accessKeys')]
        return self
