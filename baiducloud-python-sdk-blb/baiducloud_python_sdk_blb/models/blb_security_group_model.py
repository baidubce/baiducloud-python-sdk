"""
BlbSecurityGroupModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.blb_security_group_rule_model import BlbSecurityGroupRuleModel


class BlbSecurityGroupModel(AbstractModel):
    """
    BlbSecurityGroupModel
    """

    def __init__(
        self,
        security_group_id=None,
        security_group_name=None,
        security_group_desc=None,
        vpc_name=None,
        security_group_rules=None,
    ):
        """
        Initialize BlbSecurityGroupModel instance.

        :param security_group_id: 普通安全组ID
        :type security_group_id: str (optional)

        :param security_group_name: 普通安全组名称
        :type security_group_name: str (optional)

        :param security_group_desc: 普通安全组描述
        :type security_group_desc: str (optional)

        :param vpc_name: 私有网络VPC名称
        :type vpc_name: str (optional)

        :param security_group_rules: 普通安全组规则
        :type security_group_rules: List[BlbSecurityGroupRuleModel] (optional)
        """
        super().__init__()
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.security_group_desc = security_group_desc
        self.vpc_name = vpc_name
        self.security_group_rules = security_group_rules

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
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['securityGroupName'] = self.security_group_name
        if self.security_group_desc is not None:
            result['securityGroupDesc'] = self.security_group_desc
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.security_group_rules is not None:
            result['securityGroupRules'] = [i.to_dict() for i in self.security_group_rules]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BlbSecurityGroupModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('securityGroupName') is not None:
            self.security_group_name = m.get('securityGroupName')
        if m.get('securityGroupDesc') is not None:
            self.security_group_desc = m.get('securityGroupDesc')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('securityGroupRules') is not None:
            self.security_group_rules = [BlbSecurityGroupRuleModel().from_dict(i) for i in m.get('securityGroupRules')]
        return self
