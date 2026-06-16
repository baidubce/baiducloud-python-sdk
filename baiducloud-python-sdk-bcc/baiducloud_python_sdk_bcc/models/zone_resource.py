"""
ZoneResource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.bcc_bid_resources import BccBidResources


class ZoneResource(AbstractModel):
    """
    ZoneResource
    """

    def __init__(self, zone_name=None, bcc_resources=None):
        """
        Initialize ZoneResource instance.

        :param zone_name: 可用区名称
        :type zone_name: str (optional)

        :param bcc_resources: BCC资源列表
        :type bcc_resources: List[BccBidResources] (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.bcc_resources = bcc_resources

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
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.bcc_resources is not None:
            result['bccResources'] = [i.to_dict() for i in self.bcc_resources]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ZoneResource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('bccResources') is not None:
            self.bcc_resources = [BccBidResources().from_dict(i) for i in m.get('bccResources')]
        return self
