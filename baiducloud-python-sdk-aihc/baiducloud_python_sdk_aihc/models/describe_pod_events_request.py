"""
Request entity for DescribePodEventsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribePodEventsRequest(AbstractModel):
    """
    Request entity for DescribePodEventsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, resource_pool_id, queue_id, job_id, pod_name, start_time=None, end_time=None):
        """
        Initialize DescribePodEventsRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param job_id: 训练任务ID
        :type job_id: str (required)

        :param pod_name: 训练任务节点名称
        :type pod_name: str (required)

        :param start_time: 任务pod事件的起始时间，默认为 Pod 创建时间
        :type start_time: str (optional)

        :param end_time: 任务pod事件的结束时间，默认为 now
        :type end_time: str (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.job_id = job_id
        self.pod_name = pod_name
        self.start_time = start_time
        self.end_time = end_time

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribePodEventsRequest

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
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
