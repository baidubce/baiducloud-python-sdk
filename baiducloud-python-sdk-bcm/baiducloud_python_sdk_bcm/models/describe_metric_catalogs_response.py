"""
Request entity for DescribeMetricCatalogsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.metric_catalog import MetricCatalog
from baiducloud_python_sdk_bcm.models.metric import Metric


class DescribeMetricCatalogsResponse(BceResponse):
    """
    DescribeMetricCatalogsResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        catalogs=None,
        catalogs_name=None,
        catalogs_label=None,
        catalogs_catalogs=None,
        catalogs_metrics=None,
        catalogs_metrics_name=None,
        catalogs_metrics_label=None,
        catalogs_metrics_resource_identifiers=None,
        catalogs_metrics_metric_dimensions=None,
        catalogs_metrics_period=None,
        catalogs_metrics_period_unit=None,
        catalogs_metrics_unit=None,
    ):
        """
        Initialize DescribeMetricCatalogsResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param catalogs: 指标目录列表。目录为树形结构，可通过catalogs字段递归包含子目录
        :type catalogs: List[MetricCatalog] (optional)

        :param catalogs_name: 指标目录名称
        :type catalogs_name: str (optional)

        :param catalogs_label: 指标目录显示名称，根据locale返回中文或英文名称
        :type catalogs_label: str (optional)

        :param catalogs_catalogs: 当前目录下的子目录列表，结构与catalogs相同
        :type catalogs_catalogs: List[MetricCatalog] (optional)

        :param catalogs_metrics: 当前目录下的指标列表
        :type catalogs_metrics: List[Metric] (optional)

        :param catalogs_metrics_name: 指标名称，可作为指标数据查询接口的metricNames参数
        :type catalogs_metrics_name: str (optional)

        :param catalogs_metrics_label: 指标显示名称，根据locale返回中文或英文名称
        :type catalogs_metrics_label: str (optional)

        :param catalogs_metrics_resource_identifiers: 资源标识维度列表。查询指标数据时，过滤条件需要包含当前资源类型要求的全部资源标识维度
        :type catalogs_metrics_resource_identifiers: List[str] (optional)

        :param catalogs_metrics_metric_dimensions: 除资源标识维度以外的指标维度列表，可用于进一步筛选时序数据
        :type catalogs_metrics_metric_dimensions: List[str] (optional)

        :param catalogs_metrics_period: 指标采集周期数值
        :type catalogs_metrics_period: float (optional)

        :param catalogs_metrics_period_unit: 指标采集周期单位，例如s表示秒
        :type catalogs_metrics_period_unit: str (optional)

        :param catalogs_metrics_unit: 指标值单位，根据locale返回中文或英文单位
        :type catalogs_metrics_unit: str (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.catalogs = catalogs
        self.catalogs_name = catalogs_name
        self.catalogs_label = catalogs_label
        self.catalogs_catalogs = catalogs_catalogs
        self.catalogs_metrics = catalogs_metrics
        self.catalogs_metrics_name = catalogs_metrics_name
        self.catalogs_metrics_label = catalogs_metrics_label
        self.catalogs_metrics_resource_identifiers = catalogs_metrics_resource_identifiers
        self.catalogs_metrics_metric_dimensions = catalogs_metrics_metric_dimensions
        self.catalogs_metrics_period = catalogs_metrics_period
        self.catalogs_metrics_period_unit = catalogs_metrics_period_unit
        self.catalogs_metrics_unit = catalogs_metrics_unit

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
        if self.catalogs is not None:
            result['catalogs'] = [i.to_dict() for i in self.catalogs]
        if self.catalogs_name is not None:
            result['catalogs[].name'] = self.catalogs_name
        if self.catalogs_label is not None:
            result['catalogs[].label'] = self.catalogs_label
        if self.catalogs_catalogs is not None:
            result['catalogs[].catalogs'] = [i.to_dict() for i in self.catalogs_catalogs]
        if self.catalogs_metrics is not None:
            result['catalogs[].metrics'] = [i.to_dict() for i in self.catalogs_metrics]
        if self.catalogs_metrics_name is not None:
            result['catalogs[].metrics[].name'] = self.catalogs_metrics_name
        if self.catalogs_metrics_label is not None:
            result['catalogs[].metrics[].label'] = self.catalogs_metrics_label
        if self.catalogs_metrics_resource_identifiers is not None:
            result['catalogs[].metrics[].resourceIdentifiers'] = self.catalogs_metrics_resource_identifiers
        if self.catalogs_metrics_metric_dimensions is not None:
            result['catalogs[].metrics[].metricDimensions'] = self.catalogs_metrics_metric_dimensions
        if self.catalogs_metrics_period is not None:
            result['catalogs[].metrics[].period'] = self.catalogs_metrics_period
        if self.catalogs_metrics_period_unit is not None:
            result['catalogs[].metrics[].periodUnit'] = self.catalogs_metrics_period_unit
        if self.catalogs_metrics_unit is not None:
            result['catalogs[].metrics[].unit'] = self.catalogs_metrics_unit
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeMetricCatalogsResponse

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
        if m.get('catalogs') is not None:
            self.catalogs = [MetricCatalog().from_dict(i) for i in m.get('catalogs')]
        if m.get('catalogs[].name') is not None:
            self.catalogs_name = m.get('catalogs[].name')
        if m.get('catalogs[].label') is not None:
            self.catalogs_label = m.get('catalogs[].label')
        if m.get('catalogs[].catalogs') is not None:
            self.catalogs_catalogs = [MetricCatalog().from_dict(i) for i in m.get('catalogs[].catalogs')]
        if m.get('catalogs[].metrics') is not None:
            self.catalogs_metrics = [Metric().from_dict(i) for i in m.get('catalogs[].metrics')]
        if m.get('catalogs[].metrics[].name') is not None:
            self.catalogs_metrics_name = m.get('catalogs[].metrics[].name')
        if m.get('catalogs[].metrics[].label') is not None:
            self.catalogs_metrics_label = m.get('catalogs[].metrics[].label')
        if m.get('catalogs[].metrics[].resourceIdentifiers') is not None:
            self.catalogs_metrics_resource_identifiers = m.get('catalogs[].metrics[].resourceIdentifiers')
        if m.get('catalogs[].metrics[].metricDimensions') is not None:
            self.catalogs_metrics_metric_dimensions = m.get('catalogs[].metrics[].metricDimensions')
        if m.get('catalogs[].metrics[].period') is not None:
            self.catalogs_metrics_period = m.get('catalogs[].metrics[].period')
        if m.get('catalogs[].metrics[].periodUnit') is not None:
            self.catalogs_metrics_period_unit = m.get('catalogs[].metrics[].periodUnit')
        if m.get('catalogs[].metrics[].unit') is not None:
            self.catalogs_metrics_unit = m.get('catalogs[].metrics[].unit')
        return self
