"""
PrivateZone information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PrivateZone(AbstractModel):
    """
    PrivateZone
    """

    def __init__(self, zone_id=None, zone_name=None, record_count=None, create_time=None, update_time=None):
        """
        Initialize PrivateZone instance.

        :param zone_id: Zone的ID
        :type zone_id: str (optional)

        :param zone_name: Zone的名称
        :type zone_name: str (optional)

        :param record_count: 解析记录数
        :type record_count: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.record_count = record_count
        self.create_time = create_time
        self.update_time = update_time

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PrivateZone

        :raises TypeError: If input is not a dictionary type
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
        return self
