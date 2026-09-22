"""
FeatureSwitches information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FeatureSwitches(AbstractModel):
    """
    FeatureSwitches
    """

    def __init__(
        self,
        group_modify=None,
        cross_az_nearest=None,
        proxy_upgrade_support=None,
        recover_in_origin_support=None,
        recover_in_new_support=None,
        support_sentinel_switch=None,
        whitelist_group_support=None,
        bandwidth_modify=None,
        shadow_backup_support=None,
    ):
        """
        Initialize FeatureSwitches instance.

        :param group_modify: 热活中的实例是否可以变更规格和分片：true 符合热活变更规格与分片的版本要求，false 不满足要求
        :type group_modify: bool (optional)

        :param cross_az_nearest: true: 可以执行开启/关闭跨AZ就近访问；false: 不可以
        :type cross_az_nearest: bool (optional)

        :param proxy_upgrade_support: 是否支持 proxy 重启升级功能，true 支持
        :type proxy_upgrade_support: bool (optional)

        :param recover_in_origin_support: 是否允许原地恢复，多活或 pega 本地盘不支持原地恢复，为 false，否则为 true
        :type recover_in_origin_support: bool (optional)

        :param recover_in_new_support: 是否允许克隆恢复，都支持，为 true
        :type recover_in_new_support: bool (optional)

        :param support_sentinel_switch: 是否支持 sentinel 命令开关
        :type support_sentinel_switch: bool (optional)

        :param whitelist_group_support: 是否支持白名单分组字段，为 false 时为 3.x 老模块，需禁用分组功能
        :type whitelist_group_support: bool (optional)

        :param bandwidth_modify: 是否支持修改带宽
        :type bandwidth_modify: bool (optional)

        :param shadow_backup_support: 展示开启影子从库的按钮
        :type shadow_backup_support: bool (optional)
        """
        super().__init__()
        self.group_modify = group_modify
        self.cross_az_nearest = cross_az_nearest
        self.proxy_upgrade_support = proxy_upgrade_support
        self.recover_in_origin_support = recover_in_origin_support
        self.recover_in_new_support = recover_in_new_support
        self.support_sentinel_switch = support_sentinel_switch
        self.whitelist_group_support = whitelist_group_support
        self.bandwidth_modify = bandwidth_modify
        self.shadow_backup_support = shadow_backup_support

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
        if self.group_modify is not None:
            result['groupModify'] = self.group_modify
        if self.cross_az_nearest is not None:
            result['crossAzNearest'] = self.cross_az_nearest
        if self.proxy_upgrade_support is not None:
            result['proxyUpgradeSupport'] = self.proxy_upgrade_support
        if self.recover_in_origin_support is not None:
            result['recoverInOriginSupport'] = self.recover_in_origin_support
        if self.recover_in_new_support is not None:
            result['recoverInNewSupport'] = self.recover_in_new_support
        if self.support_sentinel_switch is not None:
            result['supportSentinelSwitch'] = self.support_sentinel_switch
        if self.whitelist_group_support is not None:
            result['whitelistGroupSupport'] = self.whitelist_group_support
        if self.bandwidth_modify is not None:
            result['bandwidthModify'] = self.bandwidth_modify
        if self.shadow_backup_support is not None:
            result['shadowBackupSupport'] = self.shadow_backup_support
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FeatureSwitches

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupModify') is not None:
            self.group_modify = m.get('groupModify')
        if m.get('crossAzNearest') is not None:
            self.cross_az_nearest = m.get('crossAzNearest')
        if m.get('proxyUpgradeSupport') is not None:
            self.proxy_upgrade_support = m.get('proxyUpgradeSupport')
        if m.get('recoverInOriginSupport') is not None:
            self.recover_in_origin_support = m.get('recoverInOriginSupport')
        if m.get('recoverInNewSupport') is not None:
            self.recover_in_new_support = m.get('recoverInNewSupport')
        if m.get('supportSentinelSwitch') is not None:
            self.support_sentinel_switch = m.get('supportSentinelSwitch')
        if m.get('whitelistGroupSupport') is not None:
            self.whitelist_group_support = m.get('whitelistGroupSupport')
        if m.get('bandwidthModify') is not None:
            self.bandwidth_modify = m.get('bandwidthModify')
        if m.get('shadowBackupSupport') is not None:
            self.shadow_backup_support = m.get('shadowBackupSupport')
        return self
