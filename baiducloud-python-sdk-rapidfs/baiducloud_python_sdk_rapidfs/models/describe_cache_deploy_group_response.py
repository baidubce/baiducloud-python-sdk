"""
Request entity for DescribeCacheDeployGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.cache_deploy_group_info import CacheDeployGroupInfo


class DescribeCacheDeployGroupResponse(BceResponse):
    """
    DescribeCacheDeployGroupResponse
    """

    def __init__(self, cache_deploy_group_info=None):
        """
        Initialize DescribeCacheDeployGroupResponse response.

        :param cache_deploy_group_info: cache_deploy_group_info field
        :type cache_deploy_group_info: CacheDeployGroupInfo (optional)
        """
        super().__init__()
        self.cache_deploy_group_info = cache_deploy_group_info

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
        if self.cache_deploy_group_info is not None:
            result['cacheDeployGroupInfo'] = self.cache_deploy_group_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeCacheDeployGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheDeployGroupInfo') is not None:
            self.cache_deploy_group_info = CacheDeployGroupInfo().from_dict(m.get('cacheDeployGroupInfo'))
        return self
