"""
Request entity for ProxyVersionUpgradeOrRestartRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProxyVersionUpgradeOrRestartRequest(AbstractModel):
    """
    Request entity for ProxyVersionUpgradeOrRestartRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, upgrade_type, proxy_list=None, is_defer=None):
        """
        Initialize ProxyVersionUpgradeOrRestartRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param proxy_list: 升级任务为空 重启任务不为空。<li>填写批量重启的proxy的showId
        :type proxy_list: List[str] (optional)

        :param upgrade_type: 任务类型。 <li>relaunch：重启proxy；<li> latest：升级proxy版本
        :type upgrade_type: str (required)

        :param is_defer: 是否延迟执行，默认false： <li>false 立即执行 <li>true 延迟执行(维护时间窗口执行)
        :type is_defer: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.proxy_list = proxy_list
        self.upgrade_type = upgrade_type
        self.is_defer = is_defer

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
        if self.proxy_list is not None:
            result['proxyList'] = self.proxy_list
        if self.upgrade_type is not None:
            result['upgradeType'] = self.upgrade_type
        if self.is_defer is not None:
            result['isDefer'] = self.is_defer
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProxyVersionUpgradeOrRestartRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('proxyList') is not None:
            self.proxy_list = m.get('proxyList')
        if m.get('upgradeType') is not None:
            self.upgrade_type = m.get('upgradeType')
        if m.get('isDefer') is not None:
            self.is_defer = m.get('isDefer')
        return self
