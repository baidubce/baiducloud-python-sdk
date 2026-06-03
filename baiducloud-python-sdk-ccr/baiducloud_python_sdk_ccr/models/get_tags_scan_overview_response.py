"""
Request entity for GetTagsScanOverviewResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.artifact_scan_overview import ArtifactScanOverview


class GetTagsScanOverviewResponse(BceResponse):
    """
    GetTagsScanOverviewResponse
    """

    def __init__(self, items=None, last_scan_time=None, page_no=None, page_size=None, summary=None, total=None):
        """
        Initialize GetTagsScanOverviewResponse response.

        :param items: 漏洞扫描结果列表
        :type items: List[ArtifactScanOverview] (optional)

        :param last_scan_time: 最近一次扫描时间
        :type last_scan_time: str (optional)

        :param page_no: 当前页，默认为1
        :type page_no: int (optional)

        :param page_size: 每页记录数，默认为10
        :type page_size: int (optional)

        :param summary: 不同严重程度的漏洞数量
        :type summary: object (optional)

        :param total: 漏洞总数
        :type total: int (optional)
        """
        super().__init__()
        self.items = items
        self.last_scan_time = last_scan_time
        self.page_no = page_no
        self.page_size = page_size
        self.summary = summary
        self.total = total

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
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        if self.last_scan_time is not None:
            result['lastScanTime'] = self.last_scan_time
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.summary is not None:
            result['summary'] = self.summary
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTagsScanOverviewResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('items') is not None:
            self.items = [ArtifactScanOverview().from_dict(i) for i in m.get('items')]
        if m.get('lastScanTime') is not None:
            self.last_scan_time = m.get('lastScanTime')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self
