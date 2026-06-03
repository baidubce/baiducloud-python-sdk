"""
Request entity for CreateCacheRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateCacheRuleRequest(AbstractModel):
    """
    Request entity for CreateCacheRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        data_src_id,
        cache_rule_name,
        type,
        client_token=None,
        directory=None,
        execute_on_create=None,
        description=None,
    ):
        """
        Initialize CreateCacheRuleRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param data_src_id: 数据源 ID
        :type data_src_id: str (required)

        :param cache_rule_name: 缓存管理规则名称
        :type cache_rule_name: str (required)

        :param type: type parameter
        :type type: str (required)

        :param directory: RapidFS 目录前缀，默认值为 /
        :type directory: str (optional)

        :param execute_on_create: 是否立即执行，默认 false
        :type execute_on_create: bool (optional)

        :param description: 缓存管理规则描述信息
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.data_src_id = data_src_id
        self.cache_rule_name = cache_rule_name
        self.type = type
        self.directory = directory
        self.execute_on_create = execute_on_create
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
        if self.cache_rule_name is not None:
            result['cacheRuleName'] = self.cache_rule_name
        if self.type is not None:
            result['type'] = self.type
        if self.directory is not None:
            result['directory'] = self.directory
        if self.execute_on_create is not None:
            result['executeOnCreate'] = self.execute_on_create
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
        :rtype: CreateCacheRuleRequest

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
        if m.get('cacheRuleName') is not None:
            self.cache_rule_name = m.get('cacheRuleName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('directory') is not None:
            self.directory = m.get('directory')
        if m.get('executeOnCreate') is not None:
            self.execute_on_create = m.get('executeOnCreate')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
