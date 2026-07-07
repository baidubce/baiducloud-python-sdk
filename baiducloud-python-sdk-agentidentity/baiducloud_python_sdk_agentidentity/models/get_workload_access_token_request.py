"""
Request entity for GetWorkloadAccessTokenRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetWorkloadAccessTokenRequest(AbstractModel):
    """
    Request entity for GetWorkloadAccessTokenRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, bce_user_id=None, agent_id=None, agent_name=None, duration_seconds=None):
        """
        Initialize GetWorkloadAccessTokenRequest request entity.

        :param bce_user_id: BCE 用户 ID（服务号调用时必填，用户身份调用不传，系统自动解析覆盖）
        :type bce_user_id: str (optional)

        :param agent_id: （二选一，优先使用）Agent ID，优先使用 ID，存在则不看 name
        :type agent_id: str (optional)

        :param agent_name: （二选一）Agent 名称
        :type agent_name: str (optional)

        :param duration_seconds: 有效期（秒），默认 3600，最小 900，最大 86400
        :type duration_seconds: int (optional)
        """
        super().__init__()
        self.bce_user_id = bce_user_id
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.duration_seconds = duration_seconds

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
        if self.bce_user_id is not None:
            result['bceUserId'] = self.bce_user_id
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.agent_name is not None:
            result['agentName'] = self.agent_name
        if self.duration_seconds is not None:
            result['durationSeconds'] = self.duration_seconds
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetWorkloadAccessTokenRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bceUserId') is not None:
            self.bce_user_id = m.get('bceUserId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')
        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')
        return self
