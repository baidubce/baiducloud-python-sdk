"""
Request entity for GetPrivateZoneResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_privatezone.models.vpc import Vpc


class GetPrivateZoneResponse(BceResponse):
    """
    GetPrivateZoneResponse
    """

    def __init__(
        self, zone_id=None, zone_name=None, record_count=None, create_time=None, update_time=None, bind_vpcs=None
    ):
        """
        Initialize GetPrivateZoneResponse response.

        :param zone_id: Zone的ID
        :type zone_id: str (optional)

        :param zone_name: Zone的名称
        :type zone_name: str (optional)

        :param record_count: 含有的解析记录总数
        :type record_count: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)

        :param bind_vpcs: 关联的Vpc列表
        :type bind_vpcs: List[Vpc] (optional)
        """
        super().__init__()
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.record_count = record_count
        self.create_time = create_time
        self.update_time = update_time
        self.bind_vpcs = bind_vpcs

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
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.record_count is not None:
            result['recordCount'] = self.record_count
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.bind_vpcs is not None:
            result['bindVpcs'] = [i.to_dict() for i in self.bind_vpcs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPrivateZoneResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('bindVpcs') is not None:
            self.bind_vpcs = [Vpc().from_dict(i) for i in m.get('bindVpcs')]
        return self
