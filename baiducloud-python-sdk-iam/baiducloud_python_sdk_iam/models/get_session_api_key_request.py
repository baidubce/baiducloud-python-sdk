"""
Request entity for GetSessionApiKeyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetSessionApiKeyRequest(AbstractModel):
    """
    Request entity for GetSessionApiKeyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, expire_in_seconds=None, acl=None):
        """
        Initialize GetSessionApiKeyRequest request entity.

        :param expire_in_seconds: expire_in_seconds parameter
        :type expire_in_seconds: int (optional)

        :param acl: acl parameter
        :type acl: str (optional)
        """
        super().__init__()
        self.expire_in_seconds = expire_in_seconds
        self.acl = acl

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSessionApiKeyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('expireInSeconds') is not None:
            self.expire_in_seconds = m.get('expireInSeconds')
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        return self
