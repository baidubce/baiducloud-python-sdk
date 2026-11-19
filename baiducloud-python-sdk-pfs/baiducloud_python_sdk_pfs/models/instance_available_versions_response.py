"""
Request entity for InstanceAvailableVersionsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.available_version import AvailableVersion


class InstanceAvailableVersionsResponse(BceResponse):
    """
    InstanceAvailableVersionsResponse
    """

    def __init__(self, request_id=None, available_versions=None, premium_version_number=None, version_pinned=None):
        """
        Initialize InstanceAvailableVersionsResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回
        :type request_id: str (optional)

        :param available_versions: 可用版本列表
        :type available_versions: List[AvailableVersion] (optional)

        :param premium_version_number: 推荐版本号
        :type premium_version_number: str (optional)

        :param version_pinned: 是否已固定版本
        :type version_pinned: bool (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.available_versions = available_versions
        self.premium_version_number = premium_version_number
        self.version_pinned = version_pinned

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.available_versions is not None:
            result['availableVersions'] = [i.to_dict() for i in self.available_versions]
        if self.premium_version_number is not None:
            result['premiumVersionNumber'] = self.premium_version_number
        if self.version_pinned is not None:
            result['versionPinned'] = self.version_pinned
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceAvailableVersionsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('availableVersions') is not None:
            self.available_versions = [AvailableVersion().from_dict(i) for i in m.get('availableVersions')]
        if m.get('premiumVersionNumber') is not None:
            self.premium_version_number = m.get('premiumVersionNumber')
        if m.get('versionPinned') is not None:
            self.version_pinned = m.get('versionPinned')
        return self
