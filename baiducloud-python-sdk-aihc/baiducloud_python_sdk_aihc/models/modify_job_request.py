"""
Request entity for ModifyJobRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyJobRequest(AbstractModel):
    """
    Request entity for ModifyJobRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, resource_pool_id, queue_id, job_id, priority):
        """
        Initialize ModifyJobRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param job_id: 训练任务ID
        :type job_id: str (required)

        :param priority: 训练任务优先级
        :type priority: str (required)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.job_id = job_id
        self.priority = priority

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
        if self.priority is not None:
            result['priority'] = self.priority
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyJobRequest

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
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self
