"""
Request entity for DeleteAppBlbIpGroupProtocolRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAppBlbIpGroupProtocolRequest(AbstractModel):
    """
    Request entity for DeleteAppBlbIpGroupProtocolRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, ip_group_id, backend_policy_id_list, client_token=None):
        """
        Initialize DeleteAppBlbIpGroupProtocolRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_group_id: 所属IP组的标识符
        :type ip_group_id: str (required)

        :param backend_policy_id_list: 要删除的IP组协议id数组
        :type backend_policy_id_list: List[str] (required)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.ip_group_id = ip_group_id
        self.backend_policy_id_list = backend_policy_id_list

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
        if self.ip_group_id is not None:
            result['ipGroupId'] = self.ip_group_id
        if self.backend_policy_id_list is not None:
            result['backendPolicyIdList'] = self.backend_policy_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAppBlbIpGroupProtocolRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        if m.get('backendPolicyIdList') is not None:
            self.backend_policy_id_list = m.get('backendPolicyIdList')
        return self
