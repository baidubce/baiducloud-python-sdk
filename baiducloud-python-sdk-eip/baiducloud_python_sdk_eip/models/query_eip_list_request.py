"""
Request entity for QueryEipListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryEipListRequest(AbstractModel):
    """
    Request entity for QueryEipListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        ip_version=None,
        eip=None,
        instance_type=None,
        instance_id=None,
        name=None,
        status=None,
        eip_ids=None,
        marker=None,
        max_keys=None,
    ):
        """
        Initialize QueryEipListRequest request entity.

        :param ip_version: ip_version parameter
        :type ip_version: str (optional)

        :param eip: eip parameter
        :type eip: str (optional)

        :param instance_type: instance_type parameter
        :type instance_type: str (optional)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param eip_ids: eip_ids parameter
        :type eip_ids: List (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.ip_version = ip_version
        self.eip = eip
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.name = name
        self.status = status
        self.eip_ids = eip_ids
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
        :rtype: QueryEipListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('eipIds') is not None:
            self.eip_ids = m.get('eipIds')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
