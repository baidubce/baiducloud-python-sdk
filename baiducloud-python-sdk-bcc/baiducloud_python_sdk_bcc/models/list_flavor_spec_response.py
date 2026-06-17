"""
Request entity for ListFlavorSpecResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.zone_resource_detail_spec import ZoneResourceDetailSpec


class ListFlavorSpecResponse(BceResponse):
    """
    ListFlavorSpecResponse
    """

    def __init__(self, zone_resources=None):
        """
        Initialize ListFlavorSpecResponse response.

        :param zone_resources: 各可用区下可用实例资源套餐规格列表
        :type zone_resources: List[ZoneResourceDetailSpec] (optional)
        """
        super().__init__()
        self.zone_resources = zone_resources

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
        if self.zone_resources is not None:
            result['zoneResources'] = [i.to_dict() for i in self.zone_resources]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListFlavorSpecResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneResources') is not None:
            self.zone_resources = [ZoneResourceDetailSpec().from_dict(i) for i in m.get('zoneResources')]
        return self
