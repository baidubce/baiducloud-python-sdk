"""
Request entity for CreateJobRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aihc.models.job_spec import JobSpec
from baiducloud_python_sdk_aihc.models.label import Label
from baiducloud_python_sdk_aihc.models.data_source import DataSource
from baiducloud_python_sdk_aihc.models.tensorboard_config import TensorboardConfig
from baiducloud_python_sdk_aihc.models.alert_config import AlertConfig
from baiducloud_python_sdk_aihc.models.advanced_settings import AdvancedSettings


class CreateJobRequest(AbstractModel):
    """
    Request entity for CreateJobRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        resource_pool_id,
        queue_id,
        name,
        queue,
        job_spec,
        command,
        job_type=None,
        labels=None,
        priority=None,
        datasources=None,
        enable_bccl=None,
        fault_tolerance=None,
        fault_tolerance_args=None,
        tensorboard_config=None,
        alert_config=None,
        retention_period=None,
        advanced_settings=None,
    ):
        """
        Initialize CreateJobRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param name: 名称
        :type name: str (required)

        :param queue: 训练任务所属队列，保持和queueID一致即可
        :type queue: str (required)

        :param job_type: 分布式框架类型，支持PyTorchJob，TFJob，MPIJob，RayJob。默认值：PyTorchJob
        :type job_type: str (optional)

        :param job_spec: job_spec parameter
        :type job_spec: JobSpec (required)

        :param command: 启动命令
        :type command: str (required)

        :param labels: labels parameter
        :type labels: List[Label] (optional)

        :param priority: 调度优先级，支持高（high）、中（normal）、低（low），默认值：normal
        :type priority: str (optional)

        :param datasources: 数据源配置，当前支持pfs、hostpath、bos、cfs、rapidfs、dataset
        :type datasources: List[DataSource] (optional)

        :param enable_bccl: enable_bccl parameter
        :type enable_bccl: bool (optional)

        :param fault_tolerance: 是否开启容错， 默认值为 关闭，目前PyTorchJob支持容错
        :type fault_tolerance: bool (optional)

        :param fault_tolerance_args: fault_tolerance_args parameter
        :type fault_tolerance_args: str (optional)

        :param tensorboard_config: tensorboard_config parameter
        :type tensorboard_config: TensorboardConfig (optional)

        :param alert_config: alert_config parameter
        :type alert_config: AlertConfig (optional)

        :param retention_period: 任务运行完成后的保留时间，参数格式参考：1m、1h、1d，分别代表1分钟、1小时、1天，RayJob暂不支持任务保留时间
        :type retention_period: str (optional)

        :param advanced_settings: advanced_settings parameter
        :type advanced_settings: AdvancedSettings (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.name = name
        self.queue = queue
        self.job_type = job_type
        self.job_spec = job_spec
        self.command = command
        self.labels = labels
        self.priority = priority
        self.datasources = datasources
        self.enable_bccl = enable_bccl
        self.fault_tolerance = fault_tolerance
        self.fault_tolerance_args = fault_tolerance_args
        self.tensorboard_config = tensorboard_config
        self.alert_config = alert_config
        self.retention_period = retention_period
        self.advanced_settings = advanced_settings

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
        if self.name is not None:
            result['name'] = self.name
        if self.queue is not None:
            result['queue'] = self.queue
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.job_spec is not None:
            result['jobSpec'] = self.job_spec.to_dict()
        if self.command is not None:
            result['command'] = self.command
        if self.labels is not None:
            result['labels'] = [i.to_dict() for i in self.labels]
        if self.priority is not None:
            result['priority'] = self.priority
        if self.datasources is not None:
            result['datasources'] = [i.to_dict() for i in self.datasources]
        if self.enable_bccl is not None:
            result['enableBccl'] = self.enable_bccl
        if self.fault_tolerance is not None:
            result['faultTolerance'] = self.fault_tolerance
        if self.fault_tolerance_args is not None:
            result['faultToleranceArgs'] = self.fault_tolerance_args
        if self.tensorboard_config is not None:
            result['tensorboardConfig'] = self.tensorboard_config.to_dict()
        if self.alert_config is not None:
            result['alertConfig'] = self.alert_config.to_dict()
        if self.retention_period is not None:
            result['retentionPeriod'] = self.retention_period
        if self.advanced_settings is not None:
            result['advancedSettings'] = self.advanced_settings.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateJobRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('queueID') is not None:
            self.queue_id = m.get('queueID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queue') is not None:
            self.queue = m.get('queue')
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('jobSpec') is not None:
            self.job_spec = JobSpec().from_dict(m.get('jobSpec'))
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('labels') is not None:
            self.labels = [Label().from_dict(i) for i in m.get('labels')]
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('datasources') is not None:
            self.datasources = [DataSource().from_dict(i) for i in m.get('datasources')]
        if m.get('enableBccl') is not None:
            self.enable_bccl = m.get('enableBccl')
        if m.get('faultTolerance') is not None:
            self.fault_tolerance = m.get('faultTolerance')
        if m.get('faultToleranceArgs') is not None:
            self.fault_tolerance_args = m.get('faultToleranceArgs')
        if m.get('tensorboardConfig') is not None:
            self.tensorboard_config = TensorboardConfig().from_dict(m.get('tensorboardConfig'))
        if m.get('alertConfig') is not None:
            self.alert_config = AlertConfig().from_dict(m.get('alertConfig'))
        if m.get('retentionPeriod') is not None:
            self.retention_period = m.get('retentionPeriod')
        if m.get('advancedSettings') is not None:
            self.advanced_settings = AdvancedSettings().from_dict(m.get('advancedSettings'))
        return self
