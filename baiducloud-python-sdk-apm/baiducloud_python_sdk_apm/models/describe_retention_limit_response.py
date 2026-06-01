"""
Request entity for DescribeRetentionLimitResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeRetentionLimitResponse(BceResponse):
    """
    DescribeRetentionLimitResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        min_trace_retention_days=None,
        max_trace_retention_days=None,
        min_metric_retention_days=None,
        max_metric_retention_days=None,
        min_doris_retention_days=None,
        max_doris_retention_days=None,
    ):
        """
        Initialize DescribeRetentionLimitResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param min_trace_retention_days: Trace保存时长最小值，单位：天
        :type min_trace_retention_days: int (optional)

        :param max_trace_retention_days: Trace保存时长最大值，单位：天
        :type max_trace_retention_days: int (optional)

        :param min_metric_retention_days: Metric保存时长最小值，单位：天
        :type min_metric_retention_days: int (optional)

        :param max_metric_retention_days: Metric保存时长最大值，单位：天
        :type max_metric_retention_days: int (optional)

        :param min_doris_retention_days: Trace表保存时长最小值，单位：天
        :type min_doris_retention_days: int (optional)

        :param max_doris_retention_days: Trace表保存时长最大值，单位：天
        :type max_doris_retention_days: int (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.min_trace_retention_days = min_trace_retention_days
        self.max_trace_retention_days = max_trace_retention_days
        self.min_metric_retention_days = min_metric_retention_days
        self.max_metric_retention_days = max_metric_retention_days
        self.min_doris_retention_days = min_doris_retention_days
        self.max_doris_retention_days = max_doris_retention_days

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.min_trace_retention_days is not None:
            result['minTraceRetentionDays'] = self.min_trace_retention_days
        if self.max_trace_retention_days is not None:
            result['maxTraceRetentionDays'] = self.max_trace_retention_days
        if self.min_metric_retention_days is not None:
            result['minMetricRetentionDays'] = self.min_metric_retention_days
        if self.max_metric_retention_days is not None:
            result['maxMetricRetentionDays'] = self.max_metric_retention_days
        if self.min_doris_retention_days is not None:
            result['minDorisRetentionDays'] = self.min_doris_retention_days
        if self.max_doris_retention_days is not None:
            result['maxDorisRetentionDays'] = self.max_doris_retention_days
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeRetentionLimitResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('minTraceRetentionDays') is not None:
            self.min_trace_retention_days = m.get('minTraceRetentionDays')
        if m.get('maxTraceRetentionDays') is not None:
            self.max_trace_retention_days = m.get('maxTraceRetentionDays')
        if m.get('minMetricRetentionDays') is not None:
            self.min_metric_retention_days = m.get('minMetricRetentionDays')
        if m.get('maxMetricRetentionDays') is not None:
            self.max_metric_retention_days = m.get('maxMetricRetentionDays')
        if m.get('minDorisRetentionDays') is not None:
            self.min_doris_retention_days = m.get('minDorisRetentionDays')
        if m.get('maxDorisRetentionDays') is not None:
            self.max_doris_retention_days = m.get('maxDorisRetentionDays')
        return self
