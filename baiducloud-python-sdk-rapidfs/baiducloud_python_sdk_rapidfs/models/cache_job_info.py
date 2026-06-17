"""
CacheJobInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CacheJobInfo(AbstractModel):
    """
    CacheJobInfo
    """

    def __init__(self, cache_job_id=None, status=None, size=None, start_time=None, end_time=None):
        """
        Initialize CacheJobInfo instance.

        :param cache_job_id: 缓存管理任务 ID
        :type cache_job_id: str (optional)

        :param status: 任务状态，见 CacheJobStatus
        :type status: str (optional)

        :param size: 任务已完成数据量，单位 Bytes
        :type size: int (optional)

        :param start_time: 任务开始时间，例如 2026-06-01T23:00:10Z
        :type start_time: str (optional)

        :param end_time: 任务结束时间，例如 2026-06-01T23:00:10Z
        :type end_time: str (optional)
        """
        super().__init__()
        self.cache_job_id = cache_job_id
        self.status = status
        self.size = size
        self.start_time = start_time
        self.end_time = end_time

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
        if self.cache_job_id is not None:
            result['cacheJobId'] = self.cache_job_id
        if self.status is not None:
            result['status'] = self.status
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheJobInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheJobId') is not None:
            self.cache_job_id = m.get('cacheJobId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
