"""
Request entity for AccountListUsingGETResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vdb.models.account import Account


class AccountListUsingGETResponse(BceResponse):
    """
    AccountListUsingGETResponse
    """

    def __init__(self, usernames=None):
        """
        Initialize AccountListUsingGETResponse response.

        :param usernames: usernames field
        :type usernames: List[Account] (optional)
        """
        super().__init__()
        self.usernames = usernames

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
        if self.usernames is not None:
            result['usernames'] = [i.to_dict() for i in self.usernames]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccountListUsingGETResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('usernames') is not None:
            self.usernames = [Account().from_dict(i) for i in m.get('usernames')]
        return self
