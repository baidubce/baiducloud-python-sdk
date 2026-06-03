"""
Request entity for ModifyMetaSyncRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyMetaSyncRuleRequest(AbstractModel):
    """
    Request entity for ModifyMetaSyncRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        data_src_id,
        meta_sync_rule_id,
        client_token=None,
        meta_sync_rule_name=None,
        interval_minutes=None,
        description=None,
    ):
        """
        Initialize ModifyMetaSyncRuleRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param data_src_id: 数据源 ID
        :type data_src_id: str (required)

        :param meta_sync_rule_id: 元数据同步规则 ID
        :type meta_sync_rule_id: str (required)

        :param meta_sync_rule_name: 修改后的同步规则名称
        :type meta_sync_rule_name: str (optional)

        :param interval_minutes: 修改后的周期同步间隔，单位 min。有效范围 [1, 28800(20 天)]。单次同步规则忽略该字段
        :type interval_minutes: int (optional)

        :param description: 修改后的描述信息
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.data_src_id = data_src_id
        self.meta_sync_rule_id = meta_sync_rule_id
        self.meta_sync_rule_name = meta_sync_rule_name
        self.interval_minutes = interval_minutes
        self.description = description

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        if self.meta_sync_rule_id is not None:
            result['metaSyncRuleId'] = self.meta_sync_rule_id
        if self.meta_sync_rule_name is not None:
            result['metaSyncRuleName'] = self.meta_sync_rule_name
        if self.interval_minutes is not None:
            result['intervalMinutes'] = self.interval_minutes
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyMetaSyncRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        if m.get('metaSyncRuleId') is not None:
            self.meta_sync_rule_id = m.get('metaSyncRuleId')
        if m.get('metaSyncRuleName') is not None:
            self.meta_sync_rule_name = m.get('metaSyncRuleName')
        if m.get('intervalMinutes') is not None:
            self.interval_minutes = m.get('intervalMinutes')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
