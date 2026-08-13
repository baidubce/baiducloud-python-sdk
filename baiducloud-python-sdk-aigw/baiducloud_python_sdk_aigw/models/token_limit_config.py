"""
TokenLimitConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TokenLimitConfig(AbstractModel):
    """
    TokenLimitConfig
    """

    def __init__(self, time_unit=None, time_window=None, token_amount=None, limits=None, token_usage_weight=None):
        """
        Initialize TokenLimitConfig instance.

        :param time_unit: 时间单位：second、minute、hour、day
        :type time_unit: str (optional)

        :param time_window: 时间窗口倍数，必须大于 0，默认为 1
        :type time_window: float (optional)

        :param token_amount: 兼容的 Total Token 阈值，与 limits 二选一
        :type token_amount: int (optional)

        :param limits: 分类型阈值，可包含 total、input、output，至少配置一项
        :type limits: Dict[str, int] (optional)

        :param token_usage_weight: Input Token 权重，可包含 uncached_input、cached_input
        :type token_usage_weight: Dict[str, float] (optional)
        """
        super().__init__()
        self.time_unit = time_unit
        self.time_window = time_window
        self.token_amount = token_amount
        self.limits = limits
        self.token_usage_weight = token_usage_weight

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
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.time_window is not None:
            result['time_window'] = self.time_window
        if self.token_amount is not None:
            result['token_amount'] = self.token_amount
        if self.limits is not None:
            result['limits'] = self.limits
        if self.token_usage_weight is not None:
            result['token_usage_weight'] = self.token_usage_weight
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TokenLimitConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('time_window') is not None:
            self.time_window = m.get('time_window')
        if m.get('token_amount') is not None:
            self.token_amount = m.get('token_amount')
        if m.get('limits') is not None:
            self.limits = m.get('limits')
        if m.get('token_usage_weight') is not None:
            self.token_usage_weight = m.get('token_usage_weight')
        return self
