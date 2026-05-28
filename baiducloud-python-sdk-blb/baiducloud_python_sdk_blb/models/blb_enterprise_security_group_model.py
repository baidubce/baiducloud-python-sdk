"""
BlbEnterpriseSecurityGroupModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.blb_enterprise_security_group_rule_model import (
    BlbEnterpriseSecurityGroupRuleModel,
)


class BlbEnterpriseSecurityGroupModel(AbstractModel):
    """
    BlbEnterpriseSecurityGroupModel
    """

    def __init__(
        self,
        enterprise_security_group_id=None,
        enterprise_security_group_name=None,
        enterprise_security_group_desc=None,
        enterprise_security_group_rules=None,
    ):
        """
        Initialize BlbEnterpriseSecurityGroupModel instance.

        :param enterprise_security_group_id: 企业安全组ID
        :type enterprise_security_group_id: str (optional)

        :param enterprise_security_group_name: 企业安全组名称
        :type enterprise_security_group_name: str (optional)

        :param enterprise_security_group_desc: 企业安全组描述
        :type enterprise_security_group_desc: str (optional)

        :param enterprise_security_group_rules: 企业安全组规则
        :type enterprise_security_group_rules: List[BlbEnterpriseSecurityGroupRuleModel] (optional)
        """
        super().__init__()
        self.enterprise_security_group_id = enterprise_security_group_id
        self.enterprise_security_group_name = enterprise_security_group_name
        self.enterprise_security_group_desc = enterprise_security_group_desc
        self.enterprise_security_group_rules = enterprise_security_group_rules

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
        if self.enterprise_security_group_id is not None:
            result['enterpriseSecurityGroupId'] = self.enterprise_security_group_id
        if self.enterprise_security_group_name is not None:
            result['enterpriseSecurityGroupName'] = self.enterprise_security_group_name
        if self.enterprise_security_group_desc is not None:
            result['enterpriseSecurityGroupDesc'] = self.enterprise_security_group_desc
        if self.enterprise_security_group_rules is not None:
            result['enterpriseSecurityGroupRules'] = [i.to_dict() for i in self.enterprise_security_group_rules]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BlbEnterpriseSecurityGroupModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enterpriseSecurityGroupId') is not None:
            self.enterprise_security_group_id = m.get('enterpriseSecurityGroupId')
        if m.get('enterpriseSecurityGroupName') is not None:
            self.enterprise_security_group_name = m.get('enterpriseSecurityGroupName')
        if m.get('enterpriseSecurityGroupDesc') is not None:
            self.enterprise_security_group_desc = m.get('enterpriseSecurityGroupDesc')
        if m.get('enterpriseSecurityGroupRules') is not None:
            self.enterprise_security_group_rules = [
                BlbEnterpriseSecurityGroupRuleModel().from_dict(i) for i in m.get('enterpriseSecurityGroupRules')
            ]
        return self
