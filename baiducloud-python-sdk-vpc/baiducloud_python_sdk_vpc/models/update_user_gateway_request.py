"""
This module provides the UpdateUserGatewayRequest class for handling user gateway update requests.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateUserGatewayRequest(AbstractModel):
    """
    Request class for updating user gateway information.
    
    Attributes:
        cgw_id (str): The ID of the customer gateway.
        client_token (str, optional): A unique token for request idempotency.
        name (str, optional): The name of the gateway.
        description (str, optional): The description of the gateway.
    """
    
    def __init__(self, cgw_id, client_token=None, name=None, description=None):
        """
        Initialize the UpdateUserGatewayRequest with gateway details.
        
        Args:
            cgw_id (str): The ID of the customer gateway.
            client_token (str, optional): A unique token for request idempotency.
            name (str, optional): The name of the gateway.
            description (str, optional): The description of the gateway.
        """
        super().__init__()
        self.cgw_id = cgw_id
        self.client_token = client_token
        self.name = name
        self.description = description

    def to_dict(self):
        """
        Convert the request object to a dictionary.
        
        Returns:
            dict: A dictionary containing the request attributes.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        """
        Populate the request object from a dictionary.
        
        Args:
            m (dict): A dictionary containing the request attributes.
            
        Returns:
            UpdateUserGatewayRequest: The populated request object.
        """
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self