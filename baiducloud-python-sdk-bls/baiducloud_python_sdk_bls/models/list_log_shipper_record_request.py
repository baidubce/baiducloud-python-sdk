"""
Request entity for ListLogShipperRecordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListLogShipperRecordRequest(AbstractModel):
    """
    Request entity for ListLogShipperRecordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_shipper_id, since_hours=None, page_no=None, page_size=None):
        """
        Initialize ListLogShipperRecordRequest request entity.

        :param log_shipper_id: log_shipper_id parameter
        :type log_shipper_id: str (required)

        :param since_hours: since_hours parameter
        :type since_hours: int (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.log_shipper_id = log_shipper_id
        self.since_hours = since_hours
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
        :rtype: ListLogShipperRecordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logShipperID') is not None:
            self.log_shipper_id = m.get('logShipperID')
        if m.get('sinceHours') is not None:
            self.since_hours = m.get('sinceHours')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
