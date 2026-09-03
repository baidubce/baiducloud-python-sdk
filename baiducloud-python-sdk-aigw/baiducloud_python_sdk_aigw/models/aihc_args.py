"""
AihcArgs information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AihcArgs(AbstractModel):
    """
    AihcArgs
    """

    def __init__(self, account_id=None, subnet_id=None, security_group_ids=None, vpc_cidr=None, domain_prefix=None):
        """
        Initialize AihcArgs instance.

        :param account_id: AIHC 账号 ID
        :type account_id: str (optional)

        :param subnet_id: AIHC 子网 ID
        :type subnet_id: str (optional)

        :param security_group_ids: AIHC 安全组 ID 列表或标识
        :type security_group_ids: str (optional)

        :param vpc_cidr: AIHC VPC CIDR
        :type vpc_cidr: str (optional)

        :param domain_prefix: 默认域名前缀
        :type domain_prefix: str (optional)
        """
        super().__init__()
        self.account_id = account_id
        self.subnet_id = subnet_id
        self.security_group_ids = security_group_ids
        self.vpc_cidr = vpc_cidr
        self.domain_prefix = domain_prefix

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
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.domain_prefix is not None:
            result['domainPrefix'] = self.domain_prefix
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AihcArgs

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('domainPrefix') is not None:
            self.domain_prefix = m.get('domainPrefix')
        return self
