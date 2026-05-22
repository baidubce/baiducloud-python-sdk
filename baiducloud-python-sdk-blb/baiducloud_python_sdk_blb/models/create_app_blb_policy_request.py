"""
Request entity for CreateAppBlbPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.create_app_policy import CreateAppPolicy


class CreateAppBlbPolicyRequest(AbstractModel):
    """
    Request entity for CreateAppBlbPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, listener_port, app_policy_vos, client_token=None, type=None):
        """
        Initialize CreateAppBlbPolicyRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param listener_port: 对应所在BLB下监听器端口号
        :type listener_port: int (required)

        :param app_policy_vos: app_policy_vos parameter
        :type app_policy_vos: List[CreateAppPolicy] (required)

        :param type: 当监听器端口下有多个协议时，type必传
        :type type: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.listener_port = listener_port
        self.app_policy_vos = app_policy_vos
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
        if self.listener_port is not None:
            result['listenerPort'] = self.listener_port
        if self.app_policy_vos is not None:
            result['appPolicyVos'] = [i.to_dict() for i in self.app_policy_vos]
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
        :rtype: CreateAppBlbPolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('appPolicyVos') is not None:
            self.app_policy_vos = [CreateAppPolicy().from_dict(i) for i in m.get('appPolicyVos')]
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
