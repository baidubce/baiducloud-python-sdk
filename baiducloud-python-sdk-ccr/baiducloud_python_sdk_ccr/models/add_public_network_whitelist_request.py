"""
Request entity for AddPublicNetworkWhitelistRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddPublicNetworkWhitelistRequest(AbstractModel):
    """
    Request entity for AddPublicNetworkWhitelistRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, ip_addr, description):
        """
        Initialize AddPublicNetworkWhitelistRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param ip_addr: 白名单IP地址，输入单个IPV4地址或CIDR地址段
        :type ip_addr: str (required)

        :param description: 白名单描述
        :type description: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.ip_addr = ip_addr
        self.description = description

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
        if self.ip_addr is not None:
            result['ipAddr'] = self.ip_addr
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddPublicNetworkWhitelistRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ipAddr') is not None:
            self.ip_addr = m.get('ipAddr')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
