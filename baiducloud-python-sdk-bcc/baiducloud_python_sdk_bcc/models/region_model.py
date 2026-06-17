"""
RegionModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RegionModel(AbstractModel):
    """
    RegionModel
    """

    def __init__(self, region_id=None, region_name=None, region_endpoint=None):
        """
        Initialize RegionModel instance.

        :param region_id: 地域ID，例：bj
        :type region_id: str (optional)

        :param region_name: 地域名称，例：华北-北京
        :type region_name: str (optional)

        :param region_endpoint: 地域对应的接入地址（Endpoint）
        :type region_endpoint: str (optional)
        """
        super().__init__()
        self.region_id = region_id
        self.region_name = region_name
        self.region_endpoint = region_endpoint

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
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.region_endpoint is not None:
            result['regionEndpoint'] = self.region_endpoint
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RegionModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('regionEndpoint') is not None:
            self.region_endpoint = m.get('regionEndpoint')
        return self
