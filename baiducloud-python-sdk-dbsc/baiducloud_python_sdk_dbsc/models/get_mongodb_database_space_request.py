"""
Request entity for GetMongodbDatabaseSpaceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetMongodbDatabaseSpaceRequest(AbstractModel):
    """
    Request entity for GetMongodbDatabaseSpaceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, node_id=None, database=None, order_by=None, order=None, page=None, page_size=None):
        """
        Initialize GetMongodbDatabaseSpaceRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)

        :param node_id: node_id parameter
        :type node_id: str (optional)

        :param database: database parameter
        :type database: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param page: page parameter
        :type page: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.node_id = node_id
        self.database = database
        self.order_by = order_by
        self.order = order
        self.page = page
        self.page_size = page_size

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
        :rtype: GetMongodbDatabaseSpaceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
