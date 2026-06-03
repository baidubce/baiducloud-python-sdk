"""
Request entity for QryL2PolExecLogRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QryL2PolExecLogRequest(AbstractModel):
    """
    Request entity for QryL2PolExecLogRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, policy_id, start_time=None, end_time=None):
        """
        Initialize QryL2PolExecLogRequest request entity.

        :param instance_id: policyId对应的pfs实例短id
        :type instance_id: str (required)

        :param policy_id: policyId
        :type policy_id: str (required)

        :param start_time: 查询日志起始时间戳(秒级)
        :type start_time: int (optional)

        :param end_time: 查询日志结束时间戳(秒级)
        :type end_time: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.policy_id = policy_id
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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
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
        :rtype: QryL2PolExecLogRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
