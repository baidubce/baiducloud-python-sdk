"""
Request entity for BatchStopTrainingTasksV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchStopTrainingTasksV2Request(AbstractModel):
    """
    Request entity for BatchStopTrainingTasksV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, queue_id, resource_pool_id, job_list, job_list_job_id):
        """
        Initialize BatchStopTrainingTasksV2Request request entity.

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param job_list: 任务 ID 列表数组，每个元素为包含 jobId 的对象
        :type job_list: List[object] (required)

        :param job_list_job_id: 单个任务的唯一标识，非空且唯一
        :type job_list_job_id: str (required)
        """
        super().__init__()
        self.queue_id = queue_id
        self.resource_pool_id = resource_pool_id
        self.job_list = job_list
        self.job_list_job_id = job_list_job_id

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
        if self.job_list is not None:
            result['jobList'] = self.job_list
        if self.job_list_job_id is not None:
            result['jobList[].jobId'] = self.job_list_job_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchStopTrainingTasksV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('queueID') is not None:
            self.queue_id = m.get('queueID')
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('jobList') is not None:
            self.job_list = m.get('jobList')
        if m.get('jobList[].jobId') is not None:
            self.job_list_job_id = m.get('jobList[].jobId')
        return self
