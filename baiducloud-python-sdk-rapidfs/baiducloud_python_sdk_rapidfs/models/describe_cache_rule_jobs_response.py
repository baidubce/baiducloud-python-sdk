"""
Request entity for DescribeCacheRuleJobsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.cache_job_info import CacheJobInfo


class DescribeCacheRuleJobsResponse(BceResponse):
    """
    DescribeCacheRuleJobsResponse
    """

    def __init__(self, cache_job_infos=None, marker=None, is_truncated=None, next_marker=None, max_keys=None):
        """
        Initialize DescribeCacheRuleJobsResponse response.

        :param cache_job_infos: 缓存管理任务信息列表，见附录 CacheJobInfo
        :type cache_job_infos: List[CacheJobInfo] (optional)

        :param marker: 当前查询起始位置
        :type marker: str (optional)

        :param is_truncated: true 表示后面还有数据，false 表示已经是最后一页
        :type is_truncated: bool (optional)

        :param next_marker: 下一页起始位置，为 null 表示后面没有数据了
        :type next_marker: str (optional)

        :param max_keys: 返回的列表元素个数
        :type max_keys: int (optional)
        """
        super().__init__()
        self.cache_job_infos = cache_job_infos
        self.marker = marker
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.max_keys = max_keys

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
        if self.cache_job_infos is not None:
            result['cacheJobInfos'] = [i.to_dict() for i in self.cache_job_infos]
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeCacheRuleJobsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheJobInfos') is not None:
            self.cache_job_infos = [CacheJobInfo().from_dict(i) for i in m.get('cacheJobInfos')]
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
