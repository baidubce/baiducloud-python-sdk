"""
Request entity for GetSessionTokenResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetSessionTokenResponse(BceResponse):
    """
    GetSessionTokenResponse
    """

    def __init__(self, credential=None):
        """
        Initialize GetSessionTokenResponse response.

        :param credential: 生成的临时身份凭证
        :type credential: str (optional)
        """
        super().__init__()
        self.credential = credential

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
        if self.credential is not None:
            result['credential'] = self.credential
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSessionTokenResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('credential') is not None:
            self.credential = m.get('credential')
        return self
