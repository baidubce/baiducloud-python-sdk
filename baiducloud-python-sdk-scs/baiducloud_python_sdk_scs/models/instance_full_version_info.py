"""
InstanceFullVersionInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceFullVersionInfo(AbstractModel):
    """
    InstanceFullVersionInfo
    """

    def __init__(
        self,
        proxy_full_version=None,
        redis_or_pega_full_verison=None,
        proxy_latest_full_version=None,
        redis_or_pega_latest_full_version=None,
        is_proxy_can_upgrade=None,
        is_redis_or_pega_can_upgrade=None,
        is_pega_can_restart=None,
    ):
        """
        Initialize InstanceFullVersionInfo instance.

        :param proxy_full_version: 当前集群代理版本，部分老集群可能为空
        :type proxy_full_version: str (optional)

        :param redis_or_pega_full_verison: 当前集群版本，部分老集群可能为空
        :type redis_or_pega_full_verison: str (optional)

        :param proxy_latest_full_version: 代理最新版本
        :type proxy_latest_full_version: str (optional)

        :param redis_or_pega_latest_full_version: 最新版本
        :type redis_or_pega_latest_full_version: str (optional)

        :param is_proxy_can_upgrade: 代理是否有更新的版本
        :type is_proxy_can_upgrade: bool (optional)

        :param is_redis_or_pega_can_upgrade: 是否有更新的版本
        :type is_redis_or_pega_can_upgrade: bool (optional)

        :param is_pega_can_restart: pega 是否可以重启
        :type is_pega_can_restart: bool (optional)
        """
        super().__init__()
        self.proxy_full_version = proxy_full_version
        self.redis_or_pega_full_verison = redis_or_pega_full_verison
        self.proxy_latest_full_version = proxy_latest_full_version
        self.redis_or_pega_latest_full_version = redis_or_pega_latest_full_version
        self.is_proxy_can_upgrade = is_proxy_can_upgrade
        self.is_redis_or_pega_can_upgrade = is_redis_or_pega_can_upgrade
        self.is_pega_can_restart = is_pega_can_restart

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
        if self.proxy_full_version is not None:
            result['proxyFullVersion'] = self.proxy_full_version
        if self.redis_or_pega_full_verison is not None:
            result['redisOrPegaFullVerison'] = self.redis_or_pega_full_verison
        if self.proxy_latest_full_version is not None:
            result['proxyLatestFullVersion'] = self.proxy_latest_full_version
        if self.redis_or_pega_latest_full_version is not None:
            result['redisOrPegaLatestFullVersion'] = self.redis_or_pega_latest_full_version
        if self.is_proxy_can_upgrade is not None:
            result['isProxyCanUpgrade'] = self.is_proxy_can_upgrade
        if self.is_redis_or_pega_can_upgrade is not None:
            result['isRedisOrPegaCanUpgrade'] = self.is_redis_or_pega_can_upgrade
        if self.is_pega_can_restart is not None:
            result['isPegaCanRestart'] = self.is_pega_can_restart
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceFullVersionInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('proxyFullVersion') is not None:
            self.proxy_full_version = m.get('proxyFullVersion')
        if m.get('redisOrPegaFullVerison') is not None:
            self.redis_or_pega_full_verison = m.get('redisOrPegaFullVerison')
        if m.get('proxyLatestFullVersion') is not None:
            self.proxy_latest_full_version = m.get('proxyLatestFullVersion')
        if m.get('redisOrPegaLatestFullVersion') is not None:
            self.redis_or_pega_latest_full_version = m.get('redisOrPegaLatestFullVersion')
        if m.get('isProxyCanUpgrade') is not None:
            self.is_proxy_can_upgrade = m.get('isProxyCanUpgrade')
        if m.get('isRedisOrPegaCanUpgrade') is not None:
            self.is_redis_or_pega_can_upgrade = m.get('isRedisOrPegaCanUpgrade')
        if m.get('isPegaCanRestart') is not None:
            self.is_pega_can_restart = m.get('isPegaCanRestart')
        return self
