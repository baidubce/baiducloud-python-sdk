"""
JobItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aihc.models.job_spec import JobSpec

from baiducloud_python_sdk_aihc.models.data_source import DataSource

from baiducloud_python_sdk_aihc.models.label import Label

from baiducloud_python_sdk_aihc.models.pod import Pod

from baiducloud_python_sdk_aihc.models.pod import Pod

from baiducloud_python_sdk_aihc.models.job_time_line import JobTimeLine


class JobItem(AbstractModel):
    """
    JobItem
    """

    def __init__(
        self,
        jobid=None,
        user_id=None,
        name=None,
        status=None,
        job_type=None,
        resource_pool_id=None,
        queue=None,
        job=None,
        created_at=None,
        finished_at=None,
        datasources=None,
        labels=None,
        priority=None,
        enable_bccl=None,
        enable_bccl_status=None,
        enable_bccl_error_reason=None,
        enable_fault_tolerance=None,
        fault_tolerance_args=None,
        pods=None,
        history_pods=None,
        job_time_line=None,
    ):
        """
        Initialize JobItem instance.

        :param jobid: 任务id
        :type jobid: str (optional)

        :param user_id: 用户id
        :type user_id: str (optional)

        :param name: 任务名称
        :type name: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param job_type: 任务类型，如：pytorchjob、mpijob等
        :type job_type: str (optional)

        :param resource_pool_id: 任务所在资源池Id
        :type resource_pool_id: str (optional)

        :param queue: 任务所在资源池队列
        :type queue: str (optional)

        :param job: job attribute
        :type job: JobSpec (optional)

        :param created_at: 任务创建时间
        :type created_at: str (optional)

        :param finished_at: 任务结束时间
        :type finished_at: str (optional)

        :param datasources: 任务的数据源配置
        :type datasources: List[DataSource] (optional)

        :param labels: 任务标签
        :type labels: List[Label] (optional)

        :param priority: 任务优先级
        :type priority: str (optional)

        :param enable_bccl: 任务是否开启了BCCL注入
        :type enable_bccl: bool (optional)

        :param enable_bccl_status: BCCL注入状态,包括:  success: 注入成功  failed: 注入失败  unknown: 还未执行注入
        :type enable_bccl_status: str (optional)

        :param enable_bccl_error_reason: BCCL注入失败原因
        :type enable_bccl_error_reason: str (optional)

        :param enable_fault_tolerance: 是否开启容错
        :type enable_fault_tolerance: bool (optional)

        :param fault_tolerance_args: 容错配置参数
        :type fault_tolerance_args: str (optional)

        :param pods: 任务Pod列表，在详情接口needDetail参数为False和查询训练任务列表接口中不返回该字段
        :type pods: List[Pod] (optional)

        :param history_pods: 历史Pod列表，在详情接口needDetail参数为False和查询训练任务列表接口中不返回该字段
        :type history_pods: List[Pod] (optional)

        :param job_time_line: 任务时间线详情信息，查询训练任务列表接口中不返回该字段
        :type job_time_line: List[JobTimeLine] (optional)
        """
        super().__init__()
        self.jobid = jobid
        self.user_id = user_id
        self.name = name
        self.status = status
        self.job_type = job_type
        self.resource_pool_id = resource_pool_id
        self.queue = queue
        self.job = job
        self.created_at = created_at
        self.finished_at = finished_at
        self.datasources = datasources
        self.labels = labels
        self.priority = priority
        self.enable_bccl = enable_bccl
        self.enable_bccl_status = enable_bccl_status
        self.enable_bccl_error_reason = enable_bccl_error_reason
        self.enable_fault_tolerance = enable_fault_tolerance
        self.fault_tolerance_args = fault_tolerance_args
        self.pods = pods
        self.history_pods = history_pods
        self.job_time_line = job_time_line

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
        if self.jobid is not None:
            result['jobid'] = self.jobid
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.resource_pool_id is not None:
            result['resourcePoolId'] = self.resource_pool_id
        if self.queue is not None:
            result['queue'] = self.queue
        if self.job is not None:
            result['Job'] = self.job.to_dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at
        if self.datasources is not None:
            result['datasources'] = [i.to_dict() for i in self.datasources]
        if self.labels is not None:
            result['labels'] = [i.to_dict() for i in self.labels]
        if self.priority is not None:
            result['priority'] = self.priority
        if self.enable_bccl is not None:
            result['enableBccl'] = self.enable_bccl
        if self.enable_bccl_status is not None:
            result['enableBcclStatus'] = self.enable_bccl_status
        if self.enable_bccl_error_reason is not None:
            result['enableBcclErrorReason'] = self.enable_bccl_error_reason
        if self.enable_fault_tolerance is not None:
            result['enableFaultTolerance'] = self.enable_fault_tolerance
        if self.fault_tolerance_args is not None:
            result['faultToleranceArgs'] = self.fault_tolerance_args
        if self.pods is not None:
            result['pods'] = [i.to_dict() for i in self.pods]
        if self.history_pods is not None:
            result['historyPods'] = [i.to_dict() for i in self.history_pods]
        if self.job_time_line is not None:
            result['jobTimeLine'] = [i.to_dict() for i in self.job_time_line]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: JobItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('jobid') is not None:
            self.jobid = m.get('jobid')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('queue') is not None:
            self.queue = m.get('queue')
        if m.get('Job') is not None:
            self.job = JobSpec().from_dict(m.get('Job'))
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')
        if m.get('datasources') is not None:
            self.datasources = [DataSource().from_dict(i) for i in m.get('datasources')]
        if m.get('labels') is not None:
            self.labels = [Label().from_dict(i) for i in m.get('labels')]
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('enableBccl') is not None:
            self.enable_bccl = m.get('enableBccl')
        if m.get('enableBcclStatus') is not None:
            self.enable_bccl_status = m.get('enableBcclStatus')
        if m.get('enableBcclErrorReason') is not None:
            self.enable_bccl_error_reason = m.get('enableBcclErrorReason')
        if m.get('enableFaultTolerance') is not None:
            self.enable_fault_tolerance = m.get('enableFaultTolerance')
        if m.get('faultToleranceArgs') is not None:
            self.fault_tolerance_args = m.get('faultToleranceArgs')
        if m.get('pods') is not None:
            self.pods = [Pod().from_dict(i) for i in m.get('pods')]
        if m.get('historyPods') is not None:
            self.history_pods = [Pod().from_dict(i) for i in m.get('historyPods')]
        if m.get('jobTimeLine') is not None:
            self.job_time_line = [JobTimeLine().from_dict(i) for i in m.get('jobTimeLine')]
        return self
