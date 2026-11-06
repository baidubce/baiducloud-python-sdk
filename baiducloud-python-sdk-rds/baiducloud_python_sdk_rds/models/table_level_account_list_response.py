"""
TableLevelAccountListResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class TableLevelAccountListResponse(BceResponse):
    """
    TableLevelAccountListResponse
    """

    def __init__(
        self,
        user=None,
        host=None,
        status=None,
        type=None,
        super_user_flag=None,
        remark=None,
        support_bns=None,
        wr_flag=None,
    ):
        """
        Initialize TableLevelAccountListResponse instance.

        :param user: 账号名
        :type user: str (optional)

        :param host: 来源主机
        :type host: str (optional)

        :param status: 账号状态
        :type status: str (optional)

        :param type: 账号类型
        :type type: str (optional)

        :param super_user_flag: 是否超级用户
        :type super_user_flag: str (optional)

        :param remark: 备注
        :type remark: str (optional)

        :param support_bns: 是否支持 BNS，默认 `false`
        :type support_bns: bool (optional)

        :param wr_flag: 读写标识
        :type wr_flag: str (optional)
        """
        super().__init__()
        self.user = user
        self.host = host
        self.status = status
        self.type = type
        self.super_user_flag = super_user_flag
        self.remark = remark
        self.support_bns = support_bns
        self.wr_flag = wr_flag

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.user is not None:
            result['user'] = self.user
        if self.host is not None:
            result['host'] = self.host
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.super_user_flag is not None:
            result['superUserFlag'] = self.super_user_flag
        if self.remark is not None:
            result['remark'] = self.remark
        if self.support_bns is not None:
            result['supportBns'] = self.support_bns
        if self.wr_flag is not None:
            result['wrFlag'] = self.wr_flag
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableLevelAccountListResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('superUserFlag') is not None:
            self.super_user_flag = m.get('superUserFlag')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('supportBns') is not None:
            self.support_bns = m.get('supportBns')
        if m.get('wrFlag') is not None:
            self.wr_flag = m.get('wrFlag')
        return self
