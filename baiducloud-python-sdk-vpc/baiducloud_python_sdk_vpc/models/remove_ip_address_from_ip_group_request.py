"""
Request entity for RemoveIpAddressFromIpGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoveIpAddressFromIpGroupRequest(AbstractModel):
    """
    Request entity for RemoveIpAddressFromIpGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ip_set_id, ip_address_info, client_token=None):
        """
        Initialize RemoveIpAddressFromIpGroupRequest request entity.

        :param ip_set_id: ip_set_id parameter
        :type ip_set_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_address_info: 删除的IP地址信息，单次最多指定10个
        :type ip_address_info: List[str] (required)
        """
        super().__init__()
        self.ip_set_id = ip_set_id
        self.client_token = client_token
        self.ip_address_info = ip_address_info

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
        if self.ip_address_info is not None:
            result['ipAddressInfo'] = self.ip_address_info
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoveIpAddressFromIpGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipSetId') is not None:
            self.ip_set_id = m.get('ipSetId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipAddressInfo') is not None:
            self.ip_address_info = m.get('ipAddressInfo')
        return self
