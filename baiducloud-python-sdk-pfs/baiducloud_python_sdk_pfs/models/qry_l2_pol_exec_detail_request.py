"""
Request entity for QryL2PolExecDetailRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QryL2PolExecDetailRequest(AbstractModel):
    """
    Request entity for QryL2PolExecDetailRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, policy_id, job_id):
        """
        Initialize QryL2PolExecDetailRequest request entity.

        :param instance_id: policyId对应的pfs实例短id
        :type instance_id: str (required)

        :param policy_id: policyId
        :type policy_id: str (required)

        :param job_id: 需要查询的任务ID
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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
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
        :rtype: QryL2PolExecDetailRequest

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
