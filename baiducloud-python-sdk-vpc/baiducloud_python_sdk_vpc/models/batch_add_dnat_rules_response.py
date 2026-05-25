"""
Request entity for BatchAddDnatRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class BatchAddDnatRulesResponse(BceResponse):
    """
    BatchAddDnatRulesResponse
    """

    def __init__(self, rule_ids=None):
        """
        Initialize BatchAddDnatRulesResponse response.

        :param rule_ids: 创建的DNAT规则的ID集合
        :type rule_ids: List[str] (optional)
        """
        super().__init__()
        self.rule_ids = rule_ids

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
        if self.rule_ids is not None:
            result['ruleIds'] = self.rule_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchAddDnatRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleIds') is not None:
            self.rule_ids = m.get('ruleIds')
        return self
