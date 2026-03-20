"""
Request entity for QueryVpcIntranetIpResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.vpc_private_ip_address import VpcPrivateIpAddress


class QueryVpcIntranetIpResponse(BceResponse):
    """
    QueryVpcIntranetIpResponse
    """

    def __init__(self, vpc_private_ip_addresses=None):
        """
        Initialize QueryVpcIntranetIpResponse response.

        :param vpc_private_ip_addresses: VPC内PrivateIpAddress的列表
        :type vpc_private_ip_addresses: List[VpcPrivateIpAddress] (optional)
        """
        super().__init__()
        self.vpc_private_ip_addresses = vpc_private_ip_addresses

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpc_private_ip_addresses is not None:
            result['vpcPrivateIpAddresses'] = [i.to_dict() for i in self.vpc_private_ip_addresses]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryVpcIntranetIpResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcPrivateIpAddresses') is not None:
            self.vpc_private_ip_addresses = [
                VpcPrivateIpAddress().from_dict(i) for i in m.get('vpcPrivateIpAddresses')
            ]
        return self
