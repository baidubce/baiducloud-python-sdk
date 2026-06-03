"""
Request entity for CreateMetaSyncRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateMetaSyncRuleRequest(AbstractModel):
    """
    Request entity for CreateMetaSyncRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        data_src_id,
        meta_sync_rule_name,
        type,
        client_token=None,
        directory=None,
        interval_minutes=None,
        execute_on_create=None,
        enable_on_create=None,
        description=None,
    ):
        """
        Initialize CreateMetaSyncRuleRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param data_src_id: 数据源 ID
        :type data_src_id: str (required)

        :param meta_sync_rule_name: 元数据同步规则名称
        :type meta_sync_rule_name: str (required)

        :param type: 元数据同步规则类型，枚举值：* MANUAL：单次同步，手动执行；* PERIODIC：周期同步，自动执行
        :type type: str (required)

        :param directory: RapidFS 目录前缀，默认值为 /
        :type directory: str (optional)

        :param interval_minutes: 同步间隔时间，单位 min，默认 5min。有效范围 [1, 28800(20 天)]
        :type interval_minutes: int (optional)

        :param execute_on_create: 单次同步创建之后是否立即执行，默认 false
        :type execute_on_create: bool (optional)

        :param enable_on_create: 周期同步创建之后是否默认开启，默认 true
        :type enable_on_create: bool (optional)

        :param description: 元数据同步描述信息
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.data_src_id = data_src_id
        self.meta_sync_rule_name = meta_sync_rule_name
        self.type = type
        self.directory = directory
        self.interval_minutes = interval_minutes
        self.execute_on_create = execute_on_create
        self.enable_on_create = enable_on_create
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
        if self.meta_sync_rule_name is not None:
            result['metaSyncRuleName'] = self.meta_sync_rule_name
        if self.type is not None:
            result['type'] = self.type
        if self.directory is not None:
            result['directory'] = self.directory
        if self.interval_minutes is not None:
            result['intervalMinutes'] = self.interval_minutes
        if self.execute_on_create is not None:
            result['executeOnCreate'] = self.execute_on_create
        if self.enable_on_create is not None:
            result['enableOnCreate'] = self.enable_on_create
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
        :rtype: CreateMetaSyncRuleRequest

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
        if m.get('metaSyncRuleName') is not None:
            self.meta_sync_rule_name = m.get('metaSyncRuleName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('directory') is not None:
            self.directory = m.get('directory')
        if m.get('intervalMinutes') is not None:
            self.interval_minutes = m.get('intervalMinutes')
        if m.get('executeOnCreate') is not None:
            self.execute_on_create = m.get('executeOnCreate')
        if m.get('enableOnCreate') is not None:
            self.enable_on_create = m.get('enableOnCreate')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
