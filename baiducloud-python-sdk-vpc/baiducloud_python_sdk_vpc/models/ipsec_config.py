"""
IpsecConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpsecConfig(AbstractModel):
    """
    IpsecConfig
    """

    def __init__(self, ipsec_enc_alg=None, ipsec_auth_alg=None, ipsec_pfs=None, ipsec_lifetime=None):
        """
        Initialize IpsecConfig instance.

        :param ipsec_enc_alg: 加密算法，取值范围：aes/aes192/aes256/3des
        :type ipsec_enc_alg: str (optional)

        :param ipsec_auth_alg: 认证算法，取值范围：sha1/md5
        :type ipsec_auth_alg: str (optional)

        :param ipsec_pfs: DH分组，取值范围：group2/group5/group14/group24
        :type ipsec_pfs: str (optional)

        :param ipsec_lifetime: SA生命周期,取值范围：180-86400
        :type ipsec_lifetime: str (optional)
        """
        super().__init__()
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_pfs = ipsec_pfs
        self.ipsec_lifetime = ipsec_lifetime

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
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
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IpsecConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
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
