"""
Request entity for BatchCreationOfPermissionGroupRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cfs.models.create_access_rule_response import CreateAccessRuleResponse


class BatchCreationOfPermissionGroupRulesResponse(BceResponse):
    """
    BatchCreationOfPermissionGroupRulesResponse
    """

    def __init__(self, responses=None):
        """
        Initialize BatchCreationOfPermissionGroupRulesResponse response.

        :param responses: 按顺序返回每条权限组规则创建的结果
        :type responses: List[CreateAccessRuleResponse] (optional)
        """
        super().__init__()
        self.responses = responses

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
        if self.responses is not None:
            result['responses'] = [i.to_dict() for i in self.responses]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchCreationOfPermissionGroupRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('responses') is not None:
            self.responses = [CreateAccessRuleResponse().from_dict(i) for i in m.get('responses')]
        return self
