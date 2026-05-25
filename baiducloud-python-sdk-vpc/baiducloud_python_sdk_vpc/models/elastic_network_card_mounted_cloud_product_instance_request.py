"""
Request entity for ElasticNetworkCardMountedCloudProductInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ElasticNetworkCardMountedCloudProductInstanceRequest(AbstractModel):
    """
    Request entity for ElasticNetworkCardMountedCloudProductInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eni_id, instance_id, client_token=None, instance_type=None):
        """
        Initialize ElasticNetworkCardMountedCloudProductInstanceRequest request entity.

        :param eni_id: eni_id parameter
        :type eni_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: 绑定的云产品实例ID
        :type instance_id: str (required)

        :param instance_type: 绑定的云产品实例类型，目前取值范围为server/hpas，分别表示云主机/HPAS，默认值为server
        :type instance_type: str (optional)
        """
        super().__init__()
        self.eni_id = eni_id
        self.client_token = client_token
        self.instance_id = instance_id
        self.instance_type = instance_type

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ElasticNetworkCardMountedCloudProductInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self
