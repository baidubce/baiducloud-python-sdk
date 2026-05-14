"""
Request entity for ListSnicRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListSnicRequest(AbstractModel):
    """
    Request entity for ListSnicRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, vpc_id, name=None, ip_address=None, status=None, subnet_id=None, service=None, marker=None, max_keys=None
    ):
        """
        Initialize ListSnicRequest request entity.

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param name: name parameter
        :type name: str (optional)

        :param ip_address: ip_address parameter
        :type ip_address: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param subnet_id: subnet_id parameter
        :type subnet_id: str (optional)

        :param service: service parameter
        :type service: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.name = name
        self.ip_address = ip_address
        self.status = status
        self.subnet_id = subnet_id
        self.service = service
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
        :rtype: ListSnicRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
