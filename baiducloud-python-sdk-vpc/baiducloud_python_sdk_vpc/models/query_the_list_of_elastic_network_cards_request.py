"""
Request entity for QueryTheListOfElasticNetworkCardsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryTheListOfElasticNetworkCardsRequest(AbstractModel):
    """
    Request entity for QueryTheListOfElasticNetworkCardsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, instance_id=None, name=None, private_ip_address=None, marker=None, max_keys=None):
        """
        Initialize QueryTheListOfElasticNetworkCardsRequest request entity.

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param private_ip_address: private_ip_address parameter
        :type private_ip_address: List (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.instance_id = instance_id
        self.name = name
        self.private_ip_address = private_ip_address
        self.marker = marker
        self.max_keys = max_keys

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
        :rtype: QueryTheListOfElasticNetworkCardsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
