"""
Request entity for BindEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BindEipRequest(AbstractModel):
    """
    Request entity for BindEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eip, instance_type, instance_id, client_token=None, instance_ip=None):
        """
        Initialize BindEipRequest request entity.

        :param eip: eip parameter
        :type eip: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_type: 被绑定的实例类型
        :type instance_type: str (required)

        :param instance_id: 被绑定的实例ID
        :type instance_id: str (required)

        :param instance_ip: 实例中需要绑定EIP的IP
        :type instance_ip: str (optional)
        """
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.instance_ip = instance_ip

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['instanceIp'] = self.instance_ip
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceIp') is not None:
            self.instance_ip = m.get('instanceIp')
        return self
