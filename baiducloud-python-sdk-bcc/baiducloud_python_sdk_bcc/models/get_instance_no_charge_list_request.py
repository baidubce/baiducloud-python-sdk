"""
Request entity for GetInstanceNoChargeListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetInstanceNoChargeListRequest(AbstractModel):
    """
    Request entity for GetInstanceNoChargeListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, marker=None, max_keys=None, internal_ip=None, keypair_id=None, zone_name=None, instance_ids=None
    ):
        """
        Initialize GetInstanceNoChargeListRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param internal_ip: internal_ip parameter
        :type internal_ip: str (optional)

        :param keypair_id: keypair_id parameter
        :type keypair_id: str (optional)

        :param zone_name: zone_name parameter
        :type zone_name: str (optional)

        :param instance_ids: instance_ids parameter
        :type instance_ids: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.internal_ip = internal_ip
        self.keypair_id = keypair_id
        self.zone_name = zone_name
        self.instance_ids = instance_ids

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
        :rtype: GetInstanceNoChargeListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        return self
