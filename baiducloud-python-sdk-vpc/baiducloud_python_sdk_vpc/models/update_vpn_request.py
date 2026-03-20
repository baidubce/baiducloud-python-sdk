"""
Request entity for UpdateVpnRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateVpnRequest(AbstractModel):
    """
    Request entity for UpdateVpnRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpn_id, client_token=None, vpn_name=None, description=None):
        """
        Initialize UpdateVpnRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param vpn_name: VPN名称,不能取值\"default\",长度不超过65个字符，可由数字，字符，下划线组成
        :type vpn_name: str (optional)

        :param description: VPN描述，不超过200字符
        :type description: str (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.vpn_name = vpn_name
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
        if self.vpn_name is not None:
            result['vpnName'] = self.vpn_name
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
        :rtype: UpdateVpnRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('vpnName') is not None:
            self.vpn_name = m.get('vpnName')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
