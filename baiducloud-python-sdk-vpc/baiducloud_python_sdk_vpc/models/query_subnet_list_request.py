"""
Request entity for QuerySubnetListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QuerySubnetListRequest(AbstractModel):
    """
    Request entity for QuerySubnetListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker=None, max_keys=None, vpc_id=None, zone_name=None, subnet_type=None, subnet_ids=None):
        """
        Initialize QuerySubnetListRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (optional)

        :param zone_name: zone_name parameter
        :type zone_name: str (optional)

        :param subnet_type: subnet_type parameter
        :type subnet_type: str (optional)

        :param subnet_ids: subnet_ids parameter
        :type subnet_ids: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.vpc_id = vpc_id
        self.zone_name = zone_name
        self.subnet_type = subnet_type
        self.subnet_ids = subnet_ids

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
        :rtype: QuerySubnetListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('subnetIds') is not None:
            self.subnet_ids = m.get('subnetIds')
        return self
