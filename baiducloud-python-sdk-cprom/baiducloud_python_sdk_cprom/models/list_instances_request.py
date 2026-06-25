"""
Request entity for ListInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListInstancesRequest(AbstractModel):
    """
    Request entity for ListInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_size=None, page_no=None, order_by=None, order=None, phase=None):
        """
        Initialize ListInstancesRequest request entity.

        :param page_size: page_size parameter
        :type page_size: int (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param phase: phase parameter
        :type phase: str (optional)
        """
        super().__init__()
        self.page_size = page_size
        self.page_no = page_no
        self.order_by = order_by
        self.order = order
        self.phase = phase

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
        :rtype: ListInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self
