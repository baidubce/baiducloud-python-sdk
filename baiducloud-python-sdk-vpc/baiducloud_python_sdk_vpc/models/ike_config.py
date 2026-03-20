"""
IkeConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IkeConfig(AbstractModel):
    """
    IkeConfig
    """

    def __init__(
        self, ike_version=None, ike_mode=None, ike_enc_alg=None, ike_auth_alg=None, ike_pfs=None, ike_life_time=None
    ):
        """
        Initialize IkeConfig instance.

        :param ike_version: 版本，取值范围：v1/v2
        :type ike_version: str (optional)

        :param ike_mode: 协商模式，取值范围：main/aggressive
        :type ike_mode: str (optional)

        :param ike_enc_alg: 加密算法，取值范围：aes/aes192/aes256/3des
        :type ike_enc_alg: str (optional)

        :param ike_auth_alg: 认证算法，取值范围：sha1/md5
        :type ike_auth_alg: str (optional)

        :param ike_pfs: DH分组，取值范围：group2/group5/group14/group24
        :type ike_pfs: str (optional)

        :param ike_life_time: SA生命周期,取值范围：60-86400
        :type ike_life_time: str (optional)
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
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
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
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IkeConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
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
