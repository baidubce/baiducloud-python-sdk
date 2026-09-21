"""
Request entity for GetMongodbSpaceSummaryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetMongodbSpaceSummaryResponse(BceResponse):
    """
    GetMongodbSpaceSummaryResponse
    """

    def __init__(
        self, total_disk_size=None, used_space=None, available_space=None, available_days=None, day_grow_space_avg=None
    ):
        """
        Initialize GetMongodbSpaceSummaryResponse response.

        :param total_disk_size: 磁盘总大小（字节）
        :type total_disk_size: str (optional)

        :param used_space: 已用空间（字节）
        :type used_space: str (optional)

        :param available_space: 可用空间（字节）
        :type available_space: str (optional)

        :param available_days: 预计可用天数
        :type available_days: str (optional)

        :param day_grow_space_avg: 日均增长空间（字节）
        :type day_grow_space_avg: str (optional)
        """
        super().__init__()
        self.total_disk_size = total_disk_size
        self.used_space = used_space
        self.available_space = available_space
        self.available_days = available_days
        self.day_grow_space_avg = day_grow_space_avg

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
        if self.total_disk_size is not None:
            result['totalDiskSize'] = self.total_disk_size
        if self.used_space is not None:
            result['usedSpace'] = self.used_space
        if self.available_space is not None:
            result['availableSpace'] = self.available_space
        if self.available_days is not None:
            result['availableDays'] = self.available_days
        if self.day_grow_space_avg is not None:
            result['dayGrowSpaceAvg'] = self.day_grow_space_avg
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMongodbSpaceSummaryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalDiskSize') is not None:
            self.total_disk_size = m.get('totalDiskSize')
        if m.get('usedSpace') is not None:
            self.used_space = m.get('usedSpace')
        if m.get('availableSpace') is not None:
            self.available_space = m.get('availableSpace')
        if m.get('availableDays') is not None:
            self.available_days = m.get('availableDays')
        if m.get('dayGrowSpaceAvg') is not None:
            self.day_grow_space_avg = m.get('dayGrowSpaceAvg')
        return self
