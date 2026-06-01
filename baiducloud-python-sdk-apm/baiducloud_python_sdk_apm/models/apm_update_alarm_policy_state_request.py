"""
Request entity for ApmUpdateAlarmPolicyStateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ApmUpdateAlarmPolicyStateRequest(AbstractModel):
    """
    Request entity for ApmUpdateAlarmPolicyStateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ids, state):
        """
        Initialize ApmUpdateAlarmPolicyStateRequest request entity.

        :param ids: 策略ID列表，支持批量启停
        :type ids: List[str] (required)

        :param state: 目标状态，可选值：ENABLED-启动策略，DISABLED-停用策略
        :type state: str (required)
        """
        super().__init__()
        self.ids = ids
        self.state = state

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
        if self.ids is not None:
            result['ids'] = self.ids
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApmUpdateAlarmPolicyStateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self
