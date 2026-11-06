"""
Request entity for QueryAccountListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.account import Account


class QueryAccountListResponse(BceResponse):
    """
    QueryAccountListResponse
    """

    def __init__(self, accounts=None):
        """
        Initialize QueryAccountListResponse response.

        :param accounts: Account对象
        :type accounts: List[Account] (optional)
        """
        super().__init__()
        self.accounts = accounts

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
        if self.accounts is not None:
            result['accounts'] = [i.to_dict() for i in self.accounts]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryAccountListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accounts') is not None:
            self.accounts = [Account().from_dict(i) for i in m.get('accounts')]
        return self
