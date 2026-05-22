"""
Request entity for DeleteAppBlbPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAppBlbPolicyRequest(AbstractModel):
    """
    Request entity for DeleteAppBlbPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, port, policy_id_list, client_token=None, type=None):
        """
        Initialize DeleteAppBlbPolicyRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param port: 要删除策略前端端口
        :type port: int (required)

        :param policy_id_list: 所有待释放的策略标识符，一起组成一个数组
        :type policy_id_list: List[str] (required)

        :param type: 当监听器端口下有多个协议时，type必传
        :type type: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.port = port
        self.policy_id_list = policy_id_list
        self.type = type

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
        if self.policy_id_list is not None:
            result['policyIdList'] = self.policy_id_list
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAppBlbPolicyRequest

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
        if m.get('policyIdList') is not None:
            self.policy_id_list = m.get('policyIdList')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
