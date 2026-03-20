"""
Request entity for QuerySpecifiedSubnetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.subnet_detail import SubnetDetail


class QuerySpecifiedSubnetResponse(BceResponse):
    """
    QuerySpecifiedSubnetResponse
    """

    def __init__(self, subnet=None):
        """
        Initialize QuerySpecifiedSubnetResponse response.

        :param subnet: subnet field
        :type subnet: SubnetDetail (optional)
        """
        super().__init__()
        self.subnet = subnet

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
        if self.subnet is not None:
            result['subnet'] = self.subnet.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuerySpecifiedSubnetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnet') is not None:
            self.subnet = SubnetDetail().from_dict(m.get('subnet'))
        return self
