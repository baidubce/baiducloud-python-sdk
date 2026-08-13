"""
RequestRateLimitRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RequestRateLimitRule(AbstractModel):
    """
    RequestRateLimitRule
    """

    def __init__(self, match_condition=None, limit_config=None):
        """
        Initialize RequestRateLimitRule instance.

        :param match_condition: 匹配条件，包含 type、key、value
        :type match_condition: Dict[str, str] (optional)

        :param limit_config: 次数阈值配置，包含 time_unit、time_window、request_amount
        :type limit_config: Dict[str, str] (optional)
        """
        super().__init__()
        self.match_condition = match_condition
        self.limit_config = limit_config

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.match_condition is not None:
            result['match_condition'] = self.match_condition
        if self.limit_config is not None:
            result['limit_config'] = self.limit_config
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RequestRateLimitRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('match_condition') is not None:
            self.match_condition = m.get('match_condition')
        if m.get('limit_config') is not None:
            self.limit_config = m.get('limit_config')
        return self
