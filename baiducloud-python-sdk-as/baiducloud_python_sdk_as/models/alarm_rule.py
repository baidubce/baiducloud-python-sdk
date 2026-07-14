"""
AlarmRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.dimension import Dimension


class AlarmRule(AbstractModel):
    """
    AlarmRule
    """

    def __init__(
        self,
        id=None,
        index=None,
        metric=None,
        period_in_second=None,
        statistics=None,
        threshold=None,
        comparison_operator=None,
        evaluation_period_count=None,
        metric_dimensions=None,
    ):
        """
        Initialize AlarmRule instance.

        :param id: 报警规则id
        :type id: int (optional)

        :param index: 报警规则的索引，当多个规则共同组成同一报警规则，它们的索引相同
        :type index: int (optional)

        :param metric: 监控指标名称，如：vCPUUsagePercent
        :type metric: str (optional)

        :param period_in_second: 多长时间计算一次是否满足各个报警规则，即单个评估周期时长，单位s
        :type period_in_second: int (optional)

        :param statistics: 统计方式，可选值为：maximum（最大值）、minimum（最小值）、sum（和值）、average（平均值）
        :type statistics: str (optional)

        :param threshold: 报警规则的阈值
        :type threshold: str (optional)

        :param comparison_operator: 和阈值比较的算符，取值为>=、>、=、<、<=
        :type comparison_operator: str (optional)

        :param evaluation_period_count: 触发报警所需连续发生次数
        :type evaluation_period_count: int (optional)

        :param metric_dimensions: 指标维度
        :type metric_dimensions: List[Dimension] (optional)
        """
        super().__init__()
        self.id = id
        self.index = index
        self.metric = metric
        self.period_in_second = period_in_second
        self.statistics = statistics
        self.threshold = threshold
        self.comparison_operator = comparison_operator
        self.evaluation_period_count = evaluation_period_count
        self.metric_dimensions = metric_dimensions

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
        if self.id is not None:
            result['id'] = self.id
        if self.index is not None:
            result['index'] = self.index
        if self.metric is not None:
            result['metric'] = self.metric
        if self.period_in_second is not None:
            result['periodInSecond'] = self.period_in_second
        if self.statistics is not None:
            result['statistics'] = self.statistics
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator
        if self.evaluation_period_count is not None:
            result['evaluationPeriodCount'] = self.evaluation_period_count
        if self.metric_dimensions is not None:
            result['metricDimensions'] = [i.to_dict() for i in self.metric_dimensions]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('periodInSecond') is not None:
            self.period_in_second = m.get('periodInSecond')
        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')
        if m.get('evaluationPeriodCount') is not None:
            self.evaluation_period_count = m.get('evaluationPeriodCount')
        if m.get('metricDimensions') is not None:
            self.metric_dimensions = [Dimension().from_dict(i) for i in m.get('metricDimensions')]
        return self
