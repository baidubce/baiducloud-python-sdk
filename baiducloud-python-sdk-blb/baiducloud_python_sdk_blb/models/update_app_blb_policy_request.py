"""
Request entity for UpdateAppBlbPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.app_policy_for_update import AppPolicyForUpdate


class UpdateAppBlbPolicyRequest(AbstractModel):
    """
    Request entity for UpdateAppBlbPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, port, type, policy_list, client_token=None):
        """
        Initialize UpdateAppBlbPolicyRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param port: 监听端口
        :type port: int (required)

        :param type: 监听的端口所使用的协议
        :type type: str (required)

        :param policy_list: 要修改的监听策略列表
        :type policy_list: List[AppPolicyForUpdate] (required)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.port = port
        self.type = type
        self.policy_list = policy_list

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
        if self.port is not None:
            result['port'] = self.port
        if self.type is not None:
            result['type'] = self.type
        if self.policy_list is not None:
            result['policyList'] = [i.to_dict() for i in self.policy_list]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAppBlbPolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('policyList') is not None:
            self.policy_list = [AppPolicyForUpdate().from_dict(i) for i in m.get('policyList')]
        return self
