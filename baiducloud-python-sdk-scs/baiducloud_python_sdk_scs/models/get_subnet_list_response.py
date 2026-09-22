"""
Request entity for GetSubnetListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.subnet import Subnet


class GetSubnetListResponse(BceResponse):
    """
    GetSubnetListResponse
    """

    def __init__(self, subnets=None):
        """
        Initialize GetSubnetListResponse response.

        :param subnets: 子网列表
        :type subnets: List[Subnet] (optional)
        """
        super().__init__()
        self.subnets = subnets

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
            result['metadata'] = dict(self.metadata)
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSubnetListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnets') is not None:
            self.subnets = [Subnet().from_dict(i) for i in m.get('subnets')]
        return self
