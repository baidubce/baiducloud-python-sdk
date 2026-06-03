"""
Request entity for ReExecuteTriggerTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReExecuteTriggerTaskRequest(AbstractModel):
    """
    Request entity for ReExecuteTriggerTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, policy_id, job_id):
        """
        Initialize ReExecuteTriggerTaskRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param policy_id: policy_id parameter
        :type policy_id: str (required)

        :param job_id: job_id parameter
        :type job_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.policy_id = policy_id
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReExecuteTriggerTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        return self
