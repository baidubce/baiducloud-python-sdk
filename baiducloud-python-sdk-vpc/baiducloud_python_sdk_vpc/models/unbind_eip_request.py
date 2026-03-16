from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UnbindEipRequest(AbstractModel):
    """
    UnbindEipRequest class for handling EIP unbinding requests.
    
    Attributes:
        vpn_id (str): The ID of the VPN connection.
        client_token (str, optional): A unique token for preventing duplicate requests.
    """
    
    def __init__(self, vpn_id, client_token=None):
        """
        Initialize UnbindEipRequest with VPN ID and optional client token.
        
        Args:
            vpn_id (str): The ID of the VPN connection.
            client_token (str, optional): A unique token for preventing duplicate requests.
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
            UnbindEipRequest: The populated request object.
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self