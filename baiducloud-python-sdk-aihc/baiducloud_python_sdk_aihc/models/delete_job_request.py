"""
Request entity for DeleteJobRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteJobRequest(AbstractModel):
    """
    Request entity for DeleteJobRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, resource_pool_id, queue_id, job_id):
        """
        Initialize DeleteJobRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param job_id: 训练任务ID
        :type job_id: str (required)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.job_id = job_id

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteJobRequest

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
        return self
