from baiducloud_python_sdk_core.abstract_model import AbstractModel


"""
This module provides the ReleaseVpnRequest class for VPN release operations.
"""


class ReleaseVpnRequest(AbstractModel):
    """
    Request class for releasing a VPN connection.
    
    Attributes:
        vpn_id (str): The ID of the VPN to be released.
        client_token (str, optional): A unique token for client side identification.
    """
    
    def __init__(self, vpn_id, client_token=None):
        """
        Initialize the ReleaseVpnRequest with VPN ID and optional client token.
        
        Args:
            vpn_id (str): The ID of the VPN to be released.
            client_token (str, optional): A unique token for client side identification.
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token

    def to_dict(self):
        """
        Convert the request object to a dictionary.
        
        Returns:
            dict: A dictionary containing the request data.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        """
        Populate the request object from a dictionary.
        
        Args:
            m (dict): A dictionary containing the request data.
            
        Returns:
            ReleaseVpnRequest: The populated request object.
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self