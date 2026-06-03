"""
BucketLinkInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BucketLinkInfo(AbstractModel):
    """
    BucketLinkInfo
    """

    def __init__(
        self,
        bucketlink_id=None,
        bucketlink_name=None,
        instance_id=None,
        transfer_type=None,
        create_time=None,
        finish_time=None,
        conflict_policy=None,
        throughput_limit=None,
        status=None,
        src=None,
        dst=None,
        progress=None,
        report=None,
        cron=None,
        bucket_belong_user_id=None,
        lcc_id=None,
        scope=None,
    ):
        """
        Initialize BucketLinkInfo instance.

        :param bucketlink_id: 数据流动任务ID
        :type bucketlink_id: str (optional)

        :param bucketlink_name: 数据流动任务名字
        :type bucketlink_name: str (optional)

        :param instance_id: PFS实例短ID
        :type instance_id: str (optional)

        :param transfer_type: • 0 导出任务<br>• 1 导入任务
        :type transfer_type: int (optional)

        :param create_time: 数据流动任务创建时间
        :type create_time: str (optional)

        :param finish_time: 数据流动任务结束时间
        :type finish_time: str (optional)

        :param conflict_policy: 冲突策略<br>• 1 覆盖策略<br>• 2 跳过策略<br>• 3 保留两者
        :type conflict_policy: int (optional)

        :param throughput_limit: 任务吞吐上限，单位byte
        :type throughput_limit: int (optional)

        :param status: status attribute
        :type status: int (optional)

        :param src: 数据源路径
        :type src: str (optional)

        :param dst: 数据目的路径
        :type dst: str (optional)

        :param progress: 进度情况(0 ~ 100)，在运行中时生效
        :type progress: int (optional)

        :param report: 任务报告，在任务结束（已成功、任务失败、已取消）时生效
        :type report: str (optional)

        :param cron: 只有当数据流动为周期性任务时，该字段才会返回执行周期信息
        :type cron: str (optional)

        :param bucket_belong_user_id: 只有当数据流动为跨账号任务时，该字段才会返回
        :type bucket_belong_user_id: str (optional)

        :param lcc_id: 只有当数据流动为跨账号 & bucket使用了lcc专属集群，该字段才会返回
        :type lcc_id: str (optional)

        :param scope: 任务可见范围，1：主账号以及子账号全部可见，2：仅主账号和子账号可见
        :type scope: int (optional)
        """
        super().__init__()
        self.bucketlink_id = bucketlink_id
        self.bucketlink_name = bucketlink_name
        self.instance_id = instance_id
        self.transfer_type = transfer_type
        self.create_time = create_time
        self.finish_time = finish_time
        self.conflict_policy = conflict_policy
        self.throughput_limit = throughput_limit
        self.status = status
        self.src = src
        self.dst = dst
        self.progress = progress
        self.report = report
        self.cron = cron
        self.bucket_belong_user_id = bucket_belong_user_id
        self.lcc_id = lcc_id
        self.scope = scope

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
        if self.bucketlink_id is not None:
            result['bucketlinkId'] = self.bucketlink_id
        if self.bucketlink_name is not None:
            result['bucketlinkName'] = self.bucketlink_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.transfer_type is not None:
            result['transferType'] = self.transfer_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.conflict_policy is not None:
            result['conflictPolicy'] = self.conflict_policy
        if self.throughput_limit is not None:
            result['throughputLimit'] = self.throughput_limit
        if self.status is not None:
            result['status'] = self.status
        if self.src is not None:
            result['src'] = self.src
        if self.dst is not None:
            result['dst'] = self.dst
        if self.progress is not None:
            result['progress'] = self.progress
        if self.report is not None:
            result['report'] = self.report
        if self.cron is not None:
            result['cron'] = self.cron
        if self.bucket_belong_user_id is not None:
            result['bucketBelongUserId'] = self.bucket_belong_user_id
        if self.lcc_id is not None:
            result['lccId'] = self.lcc_id
        if self.scope is not None:
            result['scope'] = self.scope
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BucketLinkInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bucketlinkId') is not None:
            self.bucketlink_id = m.get('bucketlinkId')
        if m.get('bucketlinkName') is not None:
            self.bucketlink_name = m.get('bucketlinkName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('transferType') is not None:
            self.transfer_type = m.get('transferType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('conflictPolicy') is not None:
            self.conflict_policy = m.get('conflictPolicy')
        if m.get('throughputLimit') is not None:
            self.throughput_limit = m.get('throughputLimit')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('dst') is not None:
            self.dst = m.get('dst')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('report') is not None:
            self.report = m.get('report')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('bucketBelongUserId') is not None:
            self.bucket_belong_user_id = m.get('bucketBelongUserId')
        if m.get('lccId') is not None:
            self.lcc_id = m.get('lccId')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        return self
