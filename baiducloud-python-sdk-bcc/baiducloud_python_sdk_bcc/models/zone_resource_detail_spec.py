"""
ZoneResourceDetailSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.bbc_resources import BbcResources

from baiducloud_python_sdk_bcc.models.bcc_resources import BccResources


class ZoneResourceDetailSpec(AbstractModel):
    """
    ZoneResourceDetailSpec
    """

    def __init__(self, zone_name=None, ebc_resources=None, bcc_resources=None):
        """
        Initialize ZoneResourceDetailSpec instance.

        :param zone_name: 可用区名称
        :type zone_name: str (optional)

        :param ebc_resources: ebc_resources attribute
        :type ebc_resources: BbcResources (optional)

        :param bcc_resources: bcc_resources attribute
        :type bcc_resources: BccResources (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.ebc_resources = ebc_resources
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
        if self.ebc_resources is not None:
            result['ebcResources'] = self.ebc_resources.to_dict()
        if self.bcc_resources is not None:
            result['bccResources'] = self.bcc_resources.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ZoneResourceDetailSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('ebcResources') is not None:
            self.ebc_resources = BbcResources().from_dict(m.get('ebcResources'))
        if m.get('bccResources') is not None:
            self.bcc_resources = BccResources().from_dict(m.get('bccResources'))
        return self
