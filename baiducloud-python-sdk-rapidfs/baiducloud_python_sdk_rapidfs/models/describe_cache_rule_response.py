"""
Request entity for DescribeCacheRuleResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.cache_rule_info import CacheRuleInfo


class DescribeCacheRuleResponse(BceResponse):
    """
    DescribeCacheRuleResponse
    """

    def __init__(self, cache_rule_info=None):
        """
        Initialize DescribeCacheRuleResponse response.

        :param cache_rule_info: cache_rule_info field
        :type cache_rule_info: CacheRuleInfo (optional)
        """
        super().__init__()
        self.cache_rule_info = cache_rule_info

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
        if self.cache_rule_info is not None:
            result['cacheRuleInfo'] = self.cache_rule_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeCacheRuleResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheRuleInfo') is not None:
            self.cache_rule_info = CacheRuleInfo().from_dict(m.get('cacheRuleInfo'))
        return self
