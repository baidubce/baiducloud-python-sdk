"""
Request entity for DescribeJobLogsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeJobLogsRequest(AbstractModel):
    """
    Request entity for DescribeJobLogsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        resource_pool_id,
        queue_id,
        job_id,
        pod_name,
        keywords=None,
        start_time=None,
        end_time=None,
        max_lines=None,
        chunk_size=None,
        marker=None,
    ):
        """
        Initialize DescribeJobLogsRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param job_id: 训练任务ID
        :type job_id: str (required)

        :param pod_name: 训练任务节点名称
        :type pod_name: str (required)

        :param keywords: 日志关键字查询条件，用于筛选包含指定关键字的日志
        :type keywords: str (optional)

        :param start_time: 日志的起始时间，unix时间戳；未设置则返回 Pod 从启动以来的所有日志。有效的时间范围为1970年到当前时间
        :type start_time: str (optional)

        :param end_time: 日志的结束时间，unix时间戳；未设置则返回 Pod 从启动以来的所有日志。有效的时间范围为1970年到当前时间
        :type end_time: str (optional)

        :param max_lines: 日志的最大行数；未设置则返回 Pod 从启动以来的所有日志。
        :type max_lines: str (optional)

        :param chunk_size: 输出日志按着chunk数进行汇聚，例如将10行日志为1条记录，默认1，表示每一行日志作为1条记录
        :type chunk_size: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.job_id = job_id
        self.pod_name = pod_name
        self.keywords = keywords
        self.start_time = start_time
        self.end_time = end_time
        self.max_lines = max_lines
        self.chunk_size = chunk_size
        self.marker = marker

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
        if self.pod_name is not None:
            result['podName'] = self.pod_name
        if self.keywords is not None:
            result['keywords'] = self.keywords
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_lines is not None:
            result['maxLines'] = self.max_lines
        if self.chunk_size is not None:
            result['chunkSize'] = self.chunk_size
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobLogsRequest

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
        if m.get('podName') is not None:
            self.pod_name = m.get('podName')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxLines') is not None:
            self.max_lines = m.get('maxLines')
        if m.get('chunkSize') is not None:
            self.chunk_size = m.get('chunkSize')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
