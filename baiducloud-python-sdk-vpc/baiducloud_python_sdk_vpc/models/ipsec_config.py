"""
This module defines the IpsecConfig class which represents the configuration for IPsec connection.
"""
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpsecConfig(AbstractModel):
    """
    IpsecConfig class represents the configuration for IPsec connection.
    
    Attributes:
        ipsec_enc_alg (str): The encryption algorithm for IPsec.
        ipsec_auth_alg (str): The authentication algorithm for IPsec.
        ipsec_pfs (str): The Perfect Forward Secrecy configuration for IPsec.
        ipsec_lifetime (int): The lifetime of IPsec SA in seconds.
    """

    def __init__(self, ipsec_enc_alg=None, ipsec_auth_alg=None, ipsec_pfs=None, ipsec_lifetime=None):
        """
        Initialize IpsecConfig with given parameters.
        
        Args:
            ipsec_enc_alg (str, optional): The encryption algorithm for IPsec. Defaults to None.
            ipsec_auth_alg (str, optional): The authentication algorithm for IPsec. Defaults to None.
            ipsec_pfs (str, optional): The Perfect Forward Secrecy configuration for IPsec. Defaults to None.
            ipsec_lifetime (int, optional): The lifetime of IPsec SA in seconds. Defaults to None.
        """
        super().__init__()
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_pfs = ipsec_pfs
        self.ipsec_lifetime = ipsec_lifetime

    def to_dict(self):
        """
        Convert the IpsecConfig object to a dictionary.
        
        Returns:
            dict: A dictionary containing all attributes of the IpsecConfig object.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ipsec_enc_alg is not None:
            result['ipsecEncAlg'] = self.ipsec_enc_alg
        if self.ipsec_auth_alg is not None:
            result['ipsecAuthAlg'] = self.ipsec_auth_alg
        if self.ipsec_pfs is not None:
            result['ipsecPfs'] = self.ipsec_pfs
        if self.ipsec_lifetime is not None:
            result['ipsecLifetime'] = self.ipsec_lifetime
        return result

    def from_dict(self, m):
        """
        Initialize IpsecConfig object from a dictionary.
        
        Args:
            m (dict): A dictionary containing attributes to initialize the IpsecConfig object.
            
        Returns:
            IpsecConfig: The initialized IpsecConfig object.
        """
        m = m or dict()
        if m.get('ipsecEncAlg') is not None:
            self.ipsec_enc_alg = m.get('ipsecEncAlg')
        if m.get('ipsecAuthAlg') is not None:
            self.ipsec_auth_alg = m.get('ipsecAuthAlg')
        if m.get('ipsecPfs') is not None:
            self.ipsec_pfs = m.get('ipsecPfs')
        if m.get('ipsecLifetime') is not None:
            self.ipsec_lifetime = m.get('ipsecLifetime')
        return self