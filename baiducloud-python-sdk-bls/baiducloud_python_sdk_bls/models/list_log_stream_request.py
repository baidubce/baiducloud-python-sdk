"""
Request entity for ListLogStreamRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListLogStreamRequest(AbstractModel):
    """
    Request entity for ListLogStreamRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, log_store_name, project, name_pattern=None, order=None, order_by=None, page_no=None, page_size=None
    ):
        """
        Initialize ListLogStreamRequest request entity.

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (required)

        :param project: project parameter
        :type project: str (required)

        :param name_pattern: name_pattern parameter
        :type name_pattern: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.log_store_name = log_store_name
        self.project = project
        self.name_pattern = name_pattern
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
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
        :rtype: ListLogStreamRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('namePattern') is not None:
            self.name_pattern = m.get('namePattern')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
