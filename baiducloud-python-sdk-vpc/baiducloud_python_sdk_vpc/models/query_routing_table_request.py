"""
Request entity for QueryRoutingTableRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryRoutingTableRequest(AbstractModel):
    """
    Request entity for QueryRoutingTableRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, route_table_id=None, vpc_id=None):
        """
        Initialize QueryRoutingTableRequest request entity.

        :param route_table_id: route_table_id parameter
        :type route_table_id: str (optional)

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.route_table_id = route_table_id
        self.vpc_id = vpc_id

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
        :rtype: QueryRoutingTableRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeTableId') is not None:
            self.route_table_id = m.get('routeTableId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
