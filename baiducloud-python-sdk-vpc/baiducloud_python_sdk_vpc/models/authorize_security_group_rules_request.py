"""
Request entity for AuthorizeSecurityGroupRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.security_group_rule_model import SecurityGroupRuleModel


class AuthorizeSecurityGroupRulesRequest(AbstractModel):
    """
    Request entity for AuthorizeSecurityGroupRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, security_group_id, rule, sg_version=None, client_token=None):
        """
        Initialize AuthorizeSecurityGroupRulesRequest request entity.

        :param security_group_id: security_group_id parameter
        :type security_group_id: str (required)

        :param sg_version: sg_version parameter
        :type sg_version: int (optional)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param rule: rule parameter
        :type rule: SecurityGroupRuleModel (required)
        """
        super().__init__()
        self.security_group_id = security_group_id
        self.sg_version = sg_version
        self.client_token = client_token
        self.rule = rule

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
        if self.rule is not None:
            result['rule'] = self.rule.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AuthorizeSecurityGroupRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('sgVersion') is not None:
            self.sg_version = m.get('sgVersion')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('rule') is not None:
            self.rule = SecurityGroupRuleModel().from_dict(m.get('rule'))
        return self
