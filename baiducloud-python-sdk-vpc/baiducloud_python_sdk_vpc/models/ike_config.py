"""
This module provides the IkeConfig class for handling IKE configuration parameters.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IkeConfig(AbstractModel):
    """
    IKE configuration parameters class.
    
    Attributes:
        ike_version (str): IKE version
        ike_mode (str): IKE mode
        ike_enc_alg (str): IKE encryption algorithm
        ike_auth_alg (str): IKE authentication algorithm
        ike_pfs (str): IKE PFS (Perfect Forward Secrecy)
        ike_life_time (int): IKE lifetime in seconds
    """
    
    def __init__(self, ike_version=None, ike_mode=None, ike_enc_alg=None, ike_auth_alg=None, ike_pfs=None, ike_life_time=None):
        """
        Initialize IkeConfig with given parameters.
        
        Args:
            ike_version (str, optional): IKE version. Defaults to None.
            ike_mode (str, optional): IKE mode. Defaults to None.
            ike_enc_alg (str, optional): IKE encryption algorithm. Defaults to None.
            ike_auth_alg (str, optional): IKE authentication algorithm. Defaults to None.
            ike_pfs (str, optional): IKE PFS. Defaults to None.
            ike_life_time (int, optional): IKE lifetime in seconds. Defaults to None.
        """
        super().__init__()
        self.ike_version = ike_version
        self.ike_mode = ike_mode
        self.ike_enc_alg = ike_enc_alg
        self.ike_auth_alg = ike_auth_alg
        self.ike_pfs = ike_pfs
        self.ike_life_time = ike_life_time

    def to_dict(self):
        """
        Convert the IkeConfig object to a dictionary.
        
        Returns:
            dict: A dictionary containing all non-None attributes of the IkeConfig object.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ike_version is not None:
            result['ikeVersion'] = self.ike_version
        if self.ike_mode is not None:
            result['ikeMode'] = self.ike_mode
        if self.ike_enc_alg is not None:
            result['ikeEncAlg'] = self.ike_enc_alg
        if self.ike_auth_alg is not None:
            result['ikeAuthAlg'] = self.ike_auth_alg
        if self.ike_pfs is not None:
            result['ikePfs'] = self.ike_pfs
        if self.ike_life_time is not None:
            result['ikeLifeTime'] = self.ike_life_time
        return result


    def from_dict(self, m):
        """
        Initialize the IkeConfig object from a dictionary.
        
        Args:
            m (dict): A dictionary containing IKE configuration parameters.
            
        Returns:
            IkeConfig: The IkeConfig object initialized from the dictionary.
        """
        m = m or dict()
        if m.get('ikeVersion') is not None:
            self.ike_version = m.get('ikeVersion')
        if m.get('ikeMode') is not None:
            self.ike_mode = m.get('ikeMode')
        if m.get('ikeEncAlg') is not None:
            self.ike_enc_alg = m.get('ikeEncAlg')
        if m.get('ikeAuthAlg') is not None:
            self.ike_auth_alg = m.get('ikeAuthAlg')
        if m.get('ikePfs') is not None:
            self.ike_pfs = m.get('ikePfs')
        if m.get('ikeLifeTime') is not None:
            self.ike_life_time = m.get('ikeLifeTime')
        return self