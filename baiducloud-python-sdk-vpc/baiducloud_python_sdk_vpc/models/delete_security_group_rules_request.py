"""
Request entity for DeleteSecurityGroupRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteSecurityGroupRulesRequest(AbstractModel):
    """
    Request entity for DeleteSecurityGroupRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, security_group_rule_id, client_token=None, sg_version=None):
        """
        Initialize DeleteSecurityGroupRulesRequest request entity.

        :param security_group_rule_id: security_group_rule_id parameter
        :type security_group_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param sg_version: sg_version parameter
        :type sg_version: int (optional)
        """
        super().__init__()
        self.security_group_rule_id = security_group_rule_id
        self.client_token = client_token
        self.sg_version = sg_version

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteSecurityGroupRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('securityGroupRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sgVersion') is not None:
            self.sg_version = m.get('sgVersion')
        return self
