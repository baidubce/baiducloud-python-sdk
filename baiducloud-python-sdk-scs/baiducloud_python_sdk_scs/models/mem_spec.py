"""
MemSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MemSpec(AbstractModel):
    """
    MemSpec
    """

    def __init__(
        self,
        mem_usage_upper_threshold=None,
        mem_usage_down_threshold=None,
        max_node_type=None,
        min_node_type=None,
        observation_window_size_for_upper=None,
        observation_window_size_for_down=None,
    ):
        """
        Initialize MemSpec instance.

        :param mem_usage_upper_threshold: 触发规格自动扩容的内存平均利用率阈值，单位为%，取值：70、80、90    。
        :type mem_usage_upper_threshold: int (optional)

        :param mem_usage_down_threshold: 触发规格自动缩容的内存平均利用率阈值，单位为% ，取值：20、30、40  。
        :type mem_usage_down_threshold: int (optional)

        :param max_node_type: 扩容规格上限
        :type max_node_type: str (optional)

        :param min_node_type: 缩容规格下限
        :type min_node_type: str (optional)

        :param observation_window_size_for_upper: observation_window_size_for_upper attribute
        :type observation_window_size_for_upper: str (optional)

        :param observation_window_size_for_down: observation_window_size_for_down attribute
        :type observation_window_size_for_down: str (optional)
        """
        super().__init__()
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        self.mem_usage_down_threshold = mem_usage_down_threshold
        self.max_node_type = max_node_type
        self.min_node_type = min_node_type
        self.observation_window_size_for_upper = observation_window_size_for_upper
        self.observation_window_size_for_down = observation_window_size_for_down

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
        if self.mem_usage_upper_threshold is not None:
            result['memUsageUpperThreshold'] = self.mem_usage_upper_threshold
        if self.mem_usage_down_threshold is not None:
            result['memUsageDownThreshold'] = self.mem_usage_down_threshold
        if self.max_node_type is not None:
            result['maxNodeType'] = self.max_node_type
        if self.min_node_type is not None:
            result['minNodeType'] = self.min_node_type
        if self.observation_window_size_for_upper is not None:
            result['observationWindowSizeForUpper'] = self.observation_window_size_for_upper
        if self.observation_window_size_for_down is not None:
            result['observationWindowSizeForDown'] = self.observation_window_size_for_down
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MemSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('memUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('memUsageUpperThreshold')
        if m.get('memUsageDownThreshold') is not None:
            self.mem_usage_down_threshold = m.get('memUsageDownThreshold')
        if m.get('maxNodeType') is not None:
            self.max_node_type = m.get('maxNodeType')
        if m.get('minNodeType') is not None:
            self.min_node_type = m.get('minNodeType')
        if m.get('observationWindowSizeForUpper') is not None:
            self.observation_window_size_for_upper = m.get('observationWindowSizeForUpper')
        if m.get('observationWindowSizeForDown') is not None:
            self.observation_window_size_for_down = m.get('observationWindowSizeForDown')
        return self
