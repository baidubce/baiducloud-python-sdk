"""
CacheRuleInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CacheRuleInfo(AbstractModel):
    """
    CacheRuleInfo
    """

    def __init__(
        self,
        cache_rule_id=None,
        cache_rule_name=None,
        instance_id=None,
        instance_name=None,
        data_src_id=None,
        data_src_name=None,
        type=None,
        directory=None,
        status=None,
        create_time=None,
        description=None,
        last_job_status=None,
        last_job_size=None,
        last_job_start_time=None,
        last_job_end_time=None,
    ):
        """
        Initialize CacheRuleInfo instance.

        :param cache_rule_id: 缓存管理规则 ID
        :type cache_rule_id: str (optional)

        :param cache_rule_name: 缓存管理规则名称
        :type cache_rule_name: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (optional)

        :param instance_name: RapidFS 实例名称
        :type instance_name: str (optional)

        :param data_src_id: 数据源 ID
        :type data_src_id: str (optional)

        :param data_src_name: 数据源名称
        :type data_src_name: str (optional)

        :param type: type attribute
        :type type: str (optional)

        :param directory: 规则的目录前缀，为数据源目录的相对目录
        :type directory: str (optional)

        :param status: 缓存管理规则状态，见 CacheRuleStatus
        :type status: str (optional)

        :param create_time: 创建时间，例如 2026-06-01T23:00:10Z
        :type create_time: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param last_job_status: 最近一次任务状态，见 CacheJobStatus
        :type last_job_status: str (optional)

        :param last_job_size: 最近一次任务已完成数据量大小，单位 Bytes
        :type last_job_size: int (optional)

        :param last_job_start_time: 最近一次任务开始时间，例如 2026-06-01T23:00:10Z
        :type last_job_start_time: str (optional)

        :param last_job_end_time: 最近一次任务结束时间，例如 2026-06-01T23:00:10Z
        :type last_job_end_time: str (optional)
        """
        super().__init__()
        self.cache_rule_id = cache_rule_id
        self.cache_rule_name = cache_rule_name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.data_src_id = data_src_id
        self.data_src_name = data_src_name
        self.type = type
        self.directory = directory
        self.status = status
        self.create_time = create_time
        self.description = description
        self.last_job_status = last_job_status
        self.last_job_size = last_job_size
        self.last_job_start_time = last_job_start_time
        self.last_job_end_time = last_job_end_time

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
        if self.cache_rule_id is not None:
            result['cacheRuleId'] = self.cache_rule_id
        if self.cache_rule_name is not None:
            result['cacheRuleName'] = self.cache_rule_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        if self.data_src_name is not None:
            result['dataSrcName'] = self.data_src_name
        if self.type is not None:
            result['type'] = self.type
        if self.directory is not None:
            result['directory'] = self.directory
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_job_status is not None:
            result['lastJobStatus'] = self.last_job_status
        if self.last_job_size is not None:
            result['lastJobSize'] = self.last_job_size
        if self.last_job_start_time is not None:
            result['lastJobStartTime'] = self.last_job_start_time
        if self.last_job_end_time is not None:
            result['lastJobEndTime'] = self.last_job_end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheRuleInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheRuleId') is not None:
            self.cache_rule_id = m.get('cacheRuleId')
        if m.get('cacheRuleName') is not None:
            self.cache_rule_name = m.get('cacheRuleName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        if m.get('dataSrcName') is not None:
            self.data_src_name = m.get('dataSrcName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('directory') is not None:
            self.directory = m.get('directory')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastJobStatus') is not None:
            self.last_job_status = m.get('lastJobStatus')
        if m.get('lastJobSize') is not None:
            self.last_job_size = m.get('lastJobSize')
        if m.get('lastJobStartTime') is not None:
            self.last_job_start_time = m.get('lastJobStartTime')
        if m.get('lastJobEndTime') is not None:
            self.last_job_end_time = m.get('lastJobEndTime')
        return self
