"""
Request entity for AddIpAddressesToTheIpAddressGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.template_ip_address_info import TemplateIpAddressInfo


class AddIpAddressesToTheIpAddressGroupRequest(AbstractModel):
    """
    Request entity for AddIpAddressesToTheIpAddressGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ip_set_id, ip_address_info, client_token=None):
        """
        Initialize AddIpAddressesToTheIpAddressGroupRequest request entity.

        :param ip_set_id: ip_set_id parameter
        :type ip_set_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_address_info: 添加的IP地址信息，其ipVersion需与指定的IP地址组保持一致，单次最多指定10个
        :type ip_address_info: List[TemplateIpAddressInfo] (required)
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
            result['ipAddressInfo'] = [i.to_dict() for i in self.ip_address_info]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddIpAddressesToTheIpAddressGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipSetId') is not None:
            self.ip_set_id = m.get('ipSetId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipAddressInfo') is not None:
            self.ip_address_info = [TemplateIpAddressInfo().from_dict(i) for i in m.get('ipAddressInfo')]
        return self
