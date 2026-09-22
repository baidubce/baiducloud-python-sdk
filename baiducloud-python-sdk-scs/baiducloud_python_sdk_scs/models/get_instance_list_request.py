"""
Request entity for GetInstanceListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetInstanceListRequest(AbstractModel):
    """
    Request entity for GetInstanceListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker, max_keys, instance_ids, vnet_ip):
        """
        Initialize GetInstanceListRequest request entity.

        :param marker: marker parameter
        :type marker: str (required)

        :param max_keys: max_keys parameter
        :type max_keys: str (required)

        :param instance_ids: instance_ids parameter
        :type instance_ids: str (required)

        :param vnet_ip: vnet_ip parameter
        :type vnet_ip: str (required)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.instance_ids = instance_ids
        self.vnet_ip = vnet_ip

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
        :rtype: GetInstanceListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('vnetIp') is not None:
            self.vnet_ip = m.get('vnetIp')
        return self
