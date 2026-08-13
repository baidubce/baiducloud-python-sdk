"""
TokenRateLimit information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.rule_item import RuleItem


class TokenRateLimit(AbstractModel):
    """
    TokenRateLimit
    """

    def __init__(
        self,
        rule_name=None,
        enabled=None,
        pre_reserve_remaining_ratio=None,
        pre_reserve_history_window_seconds=None,
        pre_reserve_safety_factor=None,
        pre_reserve_estimation_mode=None,
        pre_reserve_initial_tokens=None,
        sliding_window_bucket_count=None,
        pre_reserve_admission_mode=None,
        pre_reserve_admission_burst_seconds=None,
        pre_reserve_retry_jitter_ms=None,
        rule_items=None,
    ):
        """
        Initialize TokenRateLimit instance.

        :param rule_name: 规则名称
        :type rule_name: str (optional)

        :param enabled: 是否启用
        :type enabled: bool (optional)

        :param pre_reserve_remaining_ratio: 动态预扣触发阈值，范围为 0～1；省略或为 0 时关闭
        :type pre_reserve_remaining_ratio: float (optional)

        :param pre_reserve_history_window_seconds: 动态预扣历史窗口，单位为秒，默认 60
        :type pre_reserve_history_window_seconds: int (optional)

        :param pre_reserve_safety_factor: 动态预扣安全系数，必须大于等于 1，默认 1.0
        :type pre_reserve_safety_factor: float (optional)

        :param pre_reserve_estimation_mode: 估算算法：historical_mean、input_character_ratio
        :type pre_reserve_estimation_mode: str (optional)

        :param pre_reserve_initial_tokens: 首请求静态预扣，包含 input、output
        :type pre_reserve_initial_tokens: Dict[str, int] (optional)

        :param sliding_window_bucket_count: legacy 模式分桶数，范围为 1～60，默认 6
        :type sliding_window_bucket_count: int (optional)

        :param pre_reserve_admission_mode: 准入模式：smooth、legacy
        :type pre_reserve_admission_mode: str (optional)

        :param pre_reserve_admission_burst_seconds: smooth 模式突发秒数，范围为 1～60
        :type pre_reserve_admission_burst_seconds: int (optional)

        :param pre_reserve_retry_jitter_ms: smooth 模式重试抖动，范围为 0～1000 毫秒
        :type pre_reserve_retry_jitter_ms: int (optional)

        :param rule_items: Token 限流规则；每项包含 match_condition 和 limit_config
        :type rule_items: List[RuleItem] (optional)
        """
        super().__init__()
        self.rule_name = rule_name
        self.enabled = enabled
        self.pre_reserve_remaining_ratio = pre_reserve_remaining_ratio
        self.pre_reserve_history_window_seconds = pre_reserve_history_window_seconds
        self.pre_reserve_safety_factor = pre_reserve_safety_factor
        self.pre_reserve_estimation_mode = pre_reserve_estimation_mode
        self.pre_reserve_initial_tokens = pre_reserve_initial_tokens
        self.sliding_window_bucket_count = sliding_window_bucket_count
        self.pre_reserve_admission_mode = pre_reserve_admission_mode
        self.pre_reserve_admission_burst_seconds = pre_reserve_admission_burst_seconds
        self.pre_reserve_retry_jitter_ms = pre_reserve_retry_jitter_ms
        self.rule_items = rule_items

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
        if self.rule_name is not None:
            result['rule_name'] = self.rule_name
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.pre_reserve_remaining_ratio is not None:
            result['pre_reserve_remaining_ratio'] = self.pre_reserve_remaining_ratio
        if self.pre_reserve_history_window_seconds is not None:
            result['pre_reserve_history_window_seconds'] = self.pre_reserve_history_window_seconds
        if self.pre_reserve_safety_factor is not None:
            result['pre_reserve_safety_factor'] = self.pre_reserve_safety_factor
        if self.pre_reserve_estimation_mode is not None:
            result['pre_reserve_estimation_mode'] = self.pre_reserve_estimation_mode
        if self.pre_reserve_initial_tokens is not None:
            result['pre_reserve_initial_tokens'] = self.pre_reserve_initial_tokens
        if self.sliding_window_bucket_count is not None:
            result['sliding_window_bucket_count'] = self.sliding_window_bucket_count
        if self.pre_reserve_admission_mode is not None:
            result['pre_reserve_admission_mode'] = self.pre_reserve_admission_mode
        if self.pre_reserve_admission_burst_seconds is not None:
            result['pre_reserve_admission_burst_seconds'] = self.pre_reserve_admission_burst_seconds
        if self.pre_reserve_retry_jitter_ms is not None:
            result['pre_reserve_retry_jitter_ms'] = self.pre_reserve_retry_jitter_ms
        if self.rule_items is not None:
            result['rule_items'] = [i.to_dict() for i in self.rule_items]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TokenRateLimit

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('rule_name') is not None:
            self.rule_name = m.get('rule_name')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('pre_reserve_remaining_ratio') is not None:
            self.pre_reserve_remaining_ratio = m.get('pre_reserve_remaining_ratio')
        if m.get('pre_reserve_history_window_seconds') is not None:
            self.pre_reserve_history_window_seconds = m.get('pre_reserve_history_window_seconds')
        if m.get('pre_reserve_safety_factor') is not None:
            self.pre_reserve_safety_factor = m.get('pre_reserve_safety_factor')
        if m.get('pre_reserve_estimation_mode') is not None:
            self.pre_reserve_estimation_mode = m.get('pre_reserve_estimation_mode')
        if m.get('pre_reserve_initial_tokens') is not None:
            self.pre_reserve_initial_tokens = m.get('pre_reserve_initial_tokens')
        if m.get('sliding_window_bucket_count') is not None:
            self.sliding_window_bucket_count = m.get('sliding_window_bucket_count')
        if m.get('pre_reserve_admission_mode') is not None:
            self.pre_reserve_admission_mode = m.get('pre_reserve_admission_mode')
        if m.get('pre_reserve_admission_burst_seconds') is not None:
            self.pre_reserve_admission_burst_seconds = m.get('pre_reserve_admission_burst_seconds')
        if m.get('pre_reserve_retry_jitter_ms') is not None:
            self.pre_reserve_retry_jitter_ms = m.get('pre_reserve_retry_jitter_ms')
        if m.get('rule_items') is not None:
            self.rule_items = [RuleItem().from_dict(i) for i in m.get('rule_items')]
        return self
