"""
Request entity for UpdPerL2BktLnkInfoRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdPerL2BktLnkInfoRequest(AbstractModel):
    """
    Request entity for UpdPerL2BktLnkInfoRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        bucket_link_id,
        new_cron=None,
        new_bucket_link_name=None,
        new_conflict_policy=None,
        new_throughput_limit_bytes=None,
        new_scope=None,
    ):
        """
        Initialize UpdPerL2BktLnkInfoRequest request entity.

        :param instance_id: 数据流动所属PFS实例ID
        :type instance_id: str (required)

        :param bucket_link_id: 需要更新的数据流动ID
        :type bucket_link_id: str (required)

        :param new_cron: 新触发周期cron表达式
        :type new_cron: str (optional)

        :param new_bucket_link_name: 新的bucketlink名字
        :type new_bucket_link_name: str (optional)

        :param new_conflict_policy: 新的冲突策略
        :type new_conflict_policy: int (optional)

        :param new_throughput_limit_bytes: 新的吞吐限制
        :type new_throughput_limit_bytes: int (optional)

        :param new_scope: 新的可见范围，设置仅对2026-01-01之后创建的数据流动任务生效。
        :type new_scope: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.bucket_link_id = bucket_link_id
        self.new_cron = new_cron
        self.new_bucket_link_name = new_bucket_link_name
        self.new_conflict_policy = new_conflict_policy
        self.new_throughput_limit_bytes = new_throughput_limit_bytes
        self.new_scope = new_scope

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
        if self.bucket_link_id is not None:
            result['bucketLinkId'] = self.bucket_link_id
        if self.new_cron is not None:
            result['newCron'] = self.new_cron
        if self.new_bucket_link_name is not None:
            result['newBucketLinkName'] = self.new_bucket_link_name
        if self.new_conflict_policy is not None:
            result['newConflictPolicy'] = self.new_conflict_policy
        if self.new_throughput_limit_bytes is not None:
            result['newThroughputLimitBytes'] = self.new_throughput_limit_bytes
        if self.new_scope is not None:
            result['newScope'] = self.new_scope
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdPerL2BktLnkInfoRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('bucketLinkId') is not None:
            self.bucket_link_id = m.get('bucketLinkId')
        if m.get('newCron') is not None:
            self.new_cron = m.get('newCron')
        if m.get('newBucketLinkName') is not None:
            self.new_bucket_link_name = m.get('newBucketLinkName')
        if m.get('newConflictPolicy') is not None:
            self.new_conflict_policy = m.get('newConflictPolicy')
        if m.get('newThroughputLimitBytes') is not None:
            self.new_throughput_limit_bytes = m.get('newThroughputLimitBytes')
        if m.get('newScope') is not None:
            self.new_scope = m.get('newScope')
        return self
