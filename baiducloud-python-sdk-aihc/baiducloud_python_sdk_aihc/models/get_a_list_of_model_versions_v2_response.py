"""
Request entity for GetAListOfModelVersionsV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aihc.models.model_version_entry import ModelVersionEntry


class GetAListOfModelVersionsV2Response(BceResponse):
    """
    GetAListOfModelVersionsV2Response
    """

    def __init__(self, total_count=None, versions=None):
        """
        Initialize GetAListOfModelVersionsV2Response response.

        :param total_count: 模型版本总数
        :type total_count: int (optional)

        :param versions: 模型版本列表
        :type versions: List[ModelVersionEntry] (optional)
        """
        super().__init__()
        self.total_count = total_count
        self.versions = versions

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.versions is not None:
            result['versions'] = [i.to_dict() for i in self.versions]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetAListOfModelVersionsV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('versions') is not None:
            self.versions = [ModelVersionEntry().from_dict(i) for i in m.get('versions')]
        return self
