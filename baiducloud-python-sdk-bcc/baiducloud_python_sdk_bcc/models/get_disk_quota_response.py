"""
Request entity for GetDiskQuotaResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.disk_info import DiskInfo


class GetDiskQuotaResponse(BceResponse):
    """
    GetDiskQuotaResponse
    """

    def __init__(self, cds_total_capacity_gb=None, cds_used_capacity_gb=None, disk_infos=None):
        """
        Initialize GetDiskQuotaResponse response.

        :param cds_total_capacity_gb: 磁盘总容量上限（GB）
        :type cds_total_capacity_gb: str (optional)

        :param cds_used_capacity_gb: 磁盘已使用总容量（GB）
        :type cds_used_capacity_gb: str (optional)

        :param disk_infos: 可用区可创建的磁盘信息
        :type disk_infos: List[DiskInfo] (optional)
        """
        super().__init__()
        self.cds_total_capacity_gb = cds_total_capacity_gb
        self.cds_used_capacity_gb = cds_used_capacity_gb
        self.disk_infos = disk_infos

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
        if self.cds_total_capacity_gb is not None:
            result['cdsTotalCapacityGB'] = self.cds_total_capacity_gb
        if self.cds_used_capacity_gb is not None:
            result['cdsUsedCapacityGB'] = self.cds_used_capacity_gb
        if self.disk_infos is not None:
            result['diskInfos'] = [i.to_dict() for i in self.disk_infos]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetDiskQuotaResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cdsTotalCapacityGB') is not None:
            self.cds_total_capacity_gb = m.get('cdsTotalCapacityGB')
        if m.get('cdsUsedCapacityGB') is not None:
            self.cds_used_capacity_gb = m.get('cdsUsedCapacityGB')
        if m.get('diskInfos') is not None:
            self.disk_infos = [DiskInfo().from_dict(i) for i in m.get('diskInfos')]
        return self
