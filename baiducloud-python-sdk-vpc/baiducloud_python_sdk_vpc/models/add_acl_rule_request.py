"""
Request entity for AddAclRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.acl_rule_request import AclRuleRequest


class AddAclRuleRequest(AbstractModel):
    """
    Request entity for AddAclRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, acl_rules, client_token=None):
        """
        Initialize AddAclRuleRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param acl_rules: ACL规则集合
        :type acl_rules: List[AclRuleRequest] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.acl_rules = acl_rules

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
        if self.acl_rules is not None:
            result['aclRules'] = [i.to_dict() for i in self.acl_rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddAclRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('aclRules') is not None:
            self.acl_rules = [AclRuleRequest().from_dict(i) for i in m.get('aclRules')]
        return self
