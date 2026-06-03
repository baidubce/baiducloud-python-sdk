"""
Request entity for DescribeMetaSyncRuleResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.meta_sync_rule_info import MetaSyncRuleInfo


class DescribeMetaSyncRuleResponse(BceResponse):
    """
    DescribeMetaSyncRuleResponse
    """

    def __init__(self, meta_sync_rule_info=None):
        """
        Initialize DescribeMetaSyncRuleResponse response.

        :param meta_sync_rule_info: meta_sync_rule_info field
        :type meta_sync_rule_info: MetaSyncRuleInfo (optional)
        """
        super().__init__()
        self.meta_sync_rule_info = meta_sync_rule_info

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
        if self.meta_sync_rule_info is not None:
            result['metaSyncRuleInfo'] = self.meta_sync_rule_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeMetaSyncRuleResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metaSyncRuleInfo') is not None:
            self.meta_sync_rule_info = MetaSyncRuleInfo().from_dict(m.get('metaSyncRuleInfo'))
        return self
