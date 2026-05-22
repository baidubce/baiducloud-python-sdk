"""
Request entity for AuthorizedEnterpriseSecurityGroupRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.enterprise_security_group_rule_model import EnterpriseSecurityGroupRuleModel


class AuthorizedEnterpriseSecurityGroupRulesRequest(AbstractModel):
    """
    Request entity for AuthorizedEnterpriseSecurityGroupRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, enterprise_security_group_id, rules, client_token=None):
        """
        Initialize AuthorizedEnterpriseSecurityGroupRulesRequest request entity.

        :param enterprise_security_group_id: enterprise_security_group_id parameter
        :type enterprise_security_group_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param rules: 待授权企业安全组规则
        :type rules: List[EnterpriseSecurityGroupRuleModel] (required)
        """
        super().__init__()
        self.enterprise_security_group_id = enterprise_security_group_id
        self.client_token = client_token
        self.rules = rules

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AuthorizedEnterpriseSecurityGroupRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enterpriseSecurityGroupId') is not None:
            self.enterprise_security_group_id = m.get('enterpriseSecurityGroupId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('rules') is not None:
            self.rules = [EnterpriseSecurityGroupRuleModel().from_dict(i) for i in m.get('rules')]
        return self
