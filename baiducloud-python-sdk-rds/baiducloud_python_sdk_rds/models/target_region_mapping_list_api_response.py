"""
Request entity for TargetRegionMappingListApiResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class TargetRegionMappingListApiResponse(BceResponse):
    """
    TargetRegionMappingListApiResponse
    """

    def __init__(self, regions=None):
        """
        Initialize TargetRegionMappingListApiResponse response.

        :param regions: 可选的目标地域列表
        :type regions: List[str] (optional)
        """
        super().__init__()
        self.regions = regions

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
        if self.regions is not None:
            result['regions'] = self.regions
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TargetRegionMappingListApiResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        return self
