"""
Request entity for ListVolumesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListVolumesRequest(AbstractModel):
    """
    Request entity for ListVolumesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        marker=None,
        max_keys=None,
        instance_id=None,
        zone_name=None,
        cluster_id=None,
        charge_filter=None,
        usage_filter=None,
        name=None,
        product_category=None,
    ):
        """
        Initialize ListVolumesRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param zone_name: zone_name parameter
        :type zone_name: str (optional)

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (optional)

        :param charge_filter: charge_filter parameter
        :type charge_filter: str (optional)

        :param usage_filter: usage_filter parameter
        :type usage_filter: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param product_category: product_category parameter
        :type product_category: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.instance_id = instance_id
        self.zone_name = zone_name
        self.cluster_id = cluster_id
        self.charge_filter = charge_filter
        self.usage_filter = usage_filter
        self.name = name
        self.product_category = product_category

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListVolumesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('chargeFilter') is not None:
            self.charge_filter = m.get('chargeFilter')
        if m.get('usageFilter') is not None:
            self.usage_filter = m.get('usageFilter')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')
        return self
