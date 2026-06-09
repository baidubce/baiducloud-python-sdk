"""
TagScanOverview information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TagScanOverview(AbstractModel):
    """
    TagScanOverview
    """

    def __init__(
        self,
        end_time=None,
        fixable=None,
        report_id=None,
        scan_status=None,
        severity=None,
        start_time=None,
        summary=None,
        total=None,
    ):
        """
        Initialize TagScanOverview instance.

        :param end_time: 漏洞扫描完成时间，格式为 `date-time`
        :type end_time: str (optional)

        :param fixable: 可修复漏洞数量
        :type fixable: int (optional)

        :param report_id: 本机扫描报告的 ID
        :type report_id: str (optional)

        :param scan_status: 报告生成状态
        :type scan_status: str (optional)

        :param severity: 漏洞等级：`Critical` 危及、`High` 严重、`Medium` 中等、`Low` 较低
        :type severity: str (optional)

        :param start_time: 漏洞扫描开始时间，格式为 `date-time`
        :type start_time: str (optional)

        :param summary: 不同严重程度的漏洞数量
        :type summary: Dict[str, int] (optional)

        :param total: 发现的漏洞总数
        :type total: int (optional)
        """
        super().__init__()
        self.end_time = end_time
        self.fixable = fixable
        self.report_id = report_id
        self.scan_status = scan_status
        self.severity = severity
        self.start_time = start_time
        self.summary = summary
        self.total = total

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
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.fixable is not None:
            result['fixable'] = self.fixable
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.scan_status is not None:
            result['scanStatus'] = self.scan_status
        if self.severity is not None:
            result['severity'] = self.severity
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.summary is not None:
            result['summary'] = self.summary
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TagScanOverview

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('fixable') is not None:
            self.fixable = m.get('fixable')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('scanStatus') is not None:
            self.scan_status = m.get('scanStatus')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self
