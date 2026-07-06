"""
Request entity for DescribeJobMetricsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeJobMetricsRequest(AbstractModel):
    """
    Request entity for DescribeJobMetricsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        resource_pool_id,
        queue_id,
        job_id,
        metric_type,
        start_time=None,
        end_time=None,
        time_step=None,
        rate_interval=None,
    ):
        """
        Initialize DescribeJobMetricsRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param job_id: 训练任务ID
        :type job_id: str (required)

        :param start_time: 可选,默认为任务启动时间
        :type start_time: str (optional)

        :param end_time: 可选,运行中的任务默认为当前时间，已停止的任务为任务的停止时间
        :type end_time: str (optional)

        :param time_step: 返回监控数据的时间间隔，默认值是 5 分钟。
        :type time_step: str (optional)

        :param metric_type: metric_type parameter
        :type metric_type: str (required)

        :param rate_interval: 指标变化周期频率，默认为5分钟
        :type rate_interval: str (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.job_id = job_id
        self.start_time = start_time
        self.end_time = end_time
        self.time_step = time_step
        self.metric_type = metric_type
        self.rate_interval = rate_interval

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
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.time_step is not None:
            result['timeStep'] = self.time_step
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.rate_interval is not None:
            result['rateInterval'] = self.rate_interval
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobMetricsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('queueID') is not None:
            self.queue_id = m.get('queueID')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('timeStep') is not None:
            self.time_step = m.get('timeStep')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('rateInterval') is not None:
            self.rate_interval = m.get('rateInterval')
        return self
