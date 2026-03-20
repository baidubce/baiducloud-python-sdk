"""
TbspIpWhitelistModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspIpWhitelistModel(AbstractModel):
    """
    TbspIpWhitelistModel
    """

    def __init__(self, ip=None, whitelist_id=None, ip_cidr=None):
        """
        Initialize TbspIpWhitelistModel instance.

        :param ip: DDoS增强防护包防护对象IP地址
        :type ip: str (optional)

        :param whitelist_id: DDoS增强防护包IP白名单ID
        :type whitelist_id: str (optional)

        :param ip_cidr: DDoS增强防护包IP白名单网段 (完整IP地址格式或IP网段格式)
        :type ip_cidr: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.whitelist_id = whitelist_id
        self.ip_cidr = ip_cidr

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.whitelist_id is not None:
            result['whitelistId'] = self.whitelist_id
        if self.ip_cidr is not None:
            result['ipCidr'] = self.ip_cidr
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TbspIpWhitelistModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('whitelistId') is not None:
            self.whitelist_id = m.get('whitelistId')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        return self
