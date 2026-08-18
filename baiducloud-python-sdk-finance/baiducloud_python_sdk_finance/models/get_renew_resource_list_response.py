"""
Request entity for GetRenewResourceListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_finance.models.renew_resource import RenewResource


class GetRenewResourceListResponse(BceResponse):
    """
    GetRenewResourceListResponse
    """

    def __init__(
        self,
        account_id=None,
        login_name=None,
        sub_account_id=None,
        sub_login_name=None,
        ou_name=None,
        page_no=None,
        page_size=None,
        total_count=None,
        resources=None,
    ):
        """
        Initialize GetRenewResourceListResponse response.

        :param account_id: 查询账户不是子账户时，返回查询账户accountId；是子账户时，返回查询账户所在企业组织的主账户的accountId
        :type account_id: str (optional)

        :param login_name: 查询账户不是子账户时，返回查询账户的登录名；是子账户时，返回查询账户所在企业组织的主账户的登录名
        :type login_name: str (optional)

        :param sub_account_id: 查询账户不是子账户时，返回”/”；是子账户时，返回查询账户的accountId
        :type sub_account_id: str (optional)

        :param sub_login_name: 查询账户不是子账户时，返回”/”；是子账户时，返回查询账户的登录名
        :type sub_login_name: str (optional)

        :param ou_name: 查询账户不是子账户时，返回”/”；是子账户时，返回查询账户所在组织单元的单元名
        :type ou_name: str (optional)

        :param page_no: 分页查询编号，从1开始计数
        :type page_no: int (optional)

        :param page_size: 分页查询分页大小
        :type page_size: int (optional)

        :param total_count: 当前查询条件总条目
        :type total_count: int (optional)

        :param resources: 资源自动续费信息详情列表
        :type resources: List[RenewResource] (optional)
        """
        super().__init__()
        self.account_id = account_id
        self.login_name = login_name
        self.sub_account_id = sub_account_id
        self.sub_login_name = sub_login_name
        self.ou_name = ou_name
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.resources = resources

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
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        if self.sub_login_name is not None:
            result['subLoginName'] = self.sub_login_name
        if self.ou_name is not None:
            result['ouName'] = self.ou_name
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.resources is not None:
            result['resources'] = [i.to_dict() for i in self.resources]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetRenewResourceListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        if m.get('subLoginName') is not None:
            self.sub_login_name = m.get('subLoginName')
        if m.get('ouName') is not None:
            self.ou_name = m.get('ouName')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('resources') is not None:
            self.resources = [RenewResource().from_dict(i) for i in m.get('resources')]
        return self
