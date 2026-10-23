"""
Request entity for CreateL3AccessRuleResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.l3_access_rule_create_result import L3AccessRuleCreateResult


class CreateL3AccessRuleResponse(BceResponse):
    """
    CreateL3AccessRuleResponse
    """

    def __init__(self, request_id=None, access_rule_id=None, responses=None):
        """
        Initialize CreateL3AccessRuleResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回
        :type request_id: str (optional)

        :param access_rule_id: 单条创建时返回的规则 ID
        :type access_rule_id: int (optional)

        :param responses: 批量创建时的逐条结果
        :type responses: list[L3AccessRuleCreateResult] (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.access_rule_id = access_rule_id
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.access_rule_id is not None:
            result['accessRuleId'] = self.access_rule_id
        if self.responses is not None:
            result['responses'] = [item.to_dict() for item in self.responses]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL3AccessRuleResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('accessRuleId') is not None:
            self.access_rule_id = m.get('accessRuleId')
        if m.get('responses') is not None:
            self.responses = [L3AccessRuleCreateResult().from_dict(item) for item in m.get('responses')]
        return self
