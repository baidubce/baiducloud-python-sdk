"""
ProxyWrFlagInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProxyWrFlagInfo(AbstractModel):
    """
    ProxyWrFlagInfo
    """

    def __init__(self, app_id=None, account=None, wr_flag=None):
        """
        Initialize ProxyWrFlagInfo instance.

        :param app_id: Proxy 实例 ID
        :type app_id: str (optional)

        :param account: 关联账号名
        :type account: str (optional)

        :param wr_flag: 读写标识
        :type wr_flag: str (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.account = account
        self.wr_flag = wr_flag

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.account is not None:
            result['account'] = self.account
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
        :rtype: ProxyWrFlagInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('wrFlag') is not None:
            self.wr_flag = m.get('wrFlag')
        return self
