"""
Request entity for QueryLogRecordResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.result_set import ResultSet
from baiducloud_python_sdk_bls.models.dataset_scan_info import DatasetScanInfo


class QueryLogRecordResponse(BceResponse):
    """
    QueryLogRecordResponse
    """

    def __init__(self, next_marker=None, result_set=None, dataset_scan_info=None):
        """
        Initialize QueryLogRecordResponse response.

        :param next_marker: 当query为检索语句时，如果还有日志数据，将会返回nextMarker字段，标记下一条位置，用于获取下一页日志数据
        :type next_marker: str (optional)

        :param result_set: result_set field
        :type result_set: ResultSet (optional)

        :param dataset_scan_info: dataset_scan_info field
        :type dataset_scan_info: DatasetScanInfo (optional)
        """
        super().__init__()
        self.next_marker = next_marker
        self.result_set = result_set
        self.dataset_scan_info = dataset_scan_info

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
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.result_set is not None:
            result['resultSet'] = self.result_set.to_dict()
        if self.dataset_scan_info is not None:
            result['datasetScanInfo'] = self.dataset_scan_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryLogRecordResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('resultSet') is not None:
            self.result_set = ResultSet().from_dict(m.get('resultSet'))
        if m.get('datasetScanInfo') is not None:
            self.dataset_scan_info = DatasetScanInfo().from_dict(m.get('datasetScanInfo'))
        return self
