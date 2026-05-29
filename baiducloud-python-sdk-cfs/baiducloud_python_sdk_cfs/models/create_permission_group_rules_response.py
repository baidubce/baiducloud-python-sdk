"""
Request entity for CreatePermissionGroupRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreatePermissionGroupRulesResponse(BceResponse):
    """
    CreatePermissionGroupRulesResponse
    """

    def __init__(self, access_rule_id=None):
        """
        Initialize CreatePermissionGroupRulesResponse response.

        :param access_rule_id: 权限组规则的标识符
        :type access_rule_id: int (optional)
        """
        super().__init__()
        self.access_rule_id = access_rule_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.access_rule_id is not None:
            result['accessRuleId'] = self.access_rule_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePermissionGroupRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessRuleId') is not None:
            self.access_rule_id = m.get('accessRuleId')
        return self
