"""
Request entity for UpdatePublicNetworkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdatePublicNetworkRequest(AbstractModel):
    """
    Request entity for UpdatePublicNetworkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, action):
        """
        Initialize UpdatePublicNetworkRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: 更新共有网络动作，取值范围：open、close，分别表示开启公有网络访问入口、关闭公有网络入口
        :type action: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action

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
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdatePublicNetworkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self
