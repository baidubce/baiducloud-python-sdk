"""
Request entity for ListTaskV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListTaskV2Request(AbstractModel):
    """
    Request entity for ListTaskV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, groupid, order_by, page_no, order=None, page_size=None, start_time=None, end_time=None):
        """
        Initialize ListTaskV2Request request entity.

        :param groupid: groupid parameter
        :type groupid: str (required)

        :param order: order parameter
        :type order: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (required)

        :param page_no: page_no parameter
        :type page_no: int (required)

        :param page_size: page_size parameter
        :type page_size: int (optional)

        :param start_time: start_time parameter
        :type start_time: str (optional)

        :param end_time: end_time parameter
        :type end_time: str (optional)
        """
        super().__init__()
        self.groupid = groupid
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

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
        :rtype: ListTaskV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupid') is not None:
            self.groupid = m.get('groupid')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
