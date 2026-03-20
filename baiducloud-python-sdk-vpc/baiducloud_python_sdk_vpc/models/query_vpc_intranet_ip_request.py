"""
Request entity for QueryVpcIntranetIpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryVpcIntranetIpRequest(AbstractModel):
    """
    Request entity for QueryVpcIntranetIpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, private_ip_addresses=None, private_ip_range=None):
        """
        Initialize QueryVpcIntranetIpRequest request entity.

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param private_ip_addresses: private_ip_addresses parameter
        :type private_ip_addresses: List (optional)

        :param private_ip_range: private_ip_range parameter
        :type private_ip_range: str (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.private_ip_addresses = private_ip_addresses
        self.private_ip_range = private_ip_range

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
        :rtype: QueryVpcIntranetIpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('privateIpAddresses') is not None:
            self.private_ip_addresses = m.get('privateIpAddresses')
        if m.get('privateIpRange') is not None:
            self.private_ip_range = m.get('privateIpRange')
        return self
