"""
Request entity for HighlyAvailableVirtualIpBindingEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HighlyAvailableVirtualIpBindingEipRequest(AbstractModel):
    """
    Request entity for HighlyAvailableVirtualIpBindingEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ha_vip_id, public_ip_address, client_token=None):
        """
        Initialize HighlyAvailableVirtualIpBindingEipRequest request entity.

        :param ha_vip_id: ha_vip_id parameter
        :type ha_vip_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param public_ip_address: 弹性公网IP的地址
        :type public_ip_address: str (required)
        """
        super().__init__()
        self.ha_vip_id = ha_vip_id
        self.client_token = client_token
        self.public_ip_address = public_ip_address

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
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HighlyAvailableVirtualIpBindingEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('haVipId') is not None:
            self.ha_vip_id = m.get('haVipId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        return self
