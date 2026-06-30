"""
Request entity for QuerySummaryOfMainAccountResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.account_limit_info import AccountLimitInfo
from baiducloud_python_sdk_iam.models.account_count_info import AccountCountInfo


class QuerySummaryOfMainAccountResponse(BceResponse):
    """
    QuerySummaryOfMainAccountResponse
    """

    def __init__(self, account_id=None, limit_info=None, count_info=None):
        """
        Initialize QuerySummaryOfMainAccountResponse response.

        :param account_id: 主账号id
        :type account_id: str (optional)

        :param limit_info: limit_info field
        :type limit_info: AccountLimitInfo (optional)

        :param count_info: count_info field
        :type count_info: AccountCountInfo (optional)
        """
        super().__init__()
        self.account_id = account_id
        self.limit_info = limit_info
        self.count_info = count_info

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
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.limit_info is not None:
            result['limitInfo'] = self.limit_info.to_dict()
        if self.count_info is not None:
            result['countInfo'] = self.count_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuerySummaryOfMainAccountResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('limitInfo') is not None:
            self.limit_info = AccountLimitInfo().from_dict(m.get('limitInfo'))
        if m.get('countInfo') is not None:
            self.count_info = AccountCountInfo().from_dict(m.get('countInfo'))
        return self
