"""
Request entity for QuerySpecifiedVpcResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.show_vpc_model import ShowVpcModel


class QuerySpecifiedVpcResponse(BceResponse):
    """
    QuerySpecifiedVpcResponse
    """

    def __init__(self, vpc=None):
        """
        Initialize QuerySpecifiedVpcResponse response.

        :param vpc: vpc field
        :type vpc: ShowVpcModel (optional)
        """
        super().__init__()
        self.vpc = vpc

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
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuerySpecifiedVpcResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpc') is not None:
            self.vpc = ShowVpcModel().from_dict(m.get('vpc'))
        return self
