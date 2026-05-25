"""
AclEntry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.acl_rule import AclRule


class AclEntry(AbstractModel):
    """
    AclEntry
    """

    def __init__(self, subnet_id=None, subnet_name=None, subnet_cidr=None, acl_rules=None):
        """
        Initialize AclEntry instance.

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param subnet_name: 子网名称
        :type subnet_name: str (optional)

        :param subnet_cidr: 子网的CIDR
        :type subnet_cidr: str (optional)

        :param acl_rules: ACL规则集合
        :type acl_rules: List[AclRule] (optional)
        """
        super().__init__()
        self.subnet_id = subnet_id
        self.subnet_name = subnet_name
        self.subnet_cidr = subnet_cidr
        self.acl_rules = acl_rules

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.subnet_name is not None:
            result['subnetName'] = self.subnet_name
        if self.subnet_cidr is not None:
            result['subnetCidr'] = self.subnet_cidr
        if self.acl_rules is not None:
            result['aclRules'] = [i.to_dict() for i in self.acl_rules]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AclEntry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('subnetName') is not None:
            self.subnet_name = m.get('subnetName')
        if m.get('subnetCidr') is not None:
            self.subnet_cidr = m.get('subnetCidr')
        if m.get('aclRules') is not None:
            self.acl_rules = [AclRule().from_dict(i) for i in m.get('aclRules')]
        return self
