"""
Request entity for ListLogShipperRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListLogShipperRequest(AbstractModel):
    """
    Request entity for ListLogShipperRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        log_shipper_id=None,
        log_shipper_name=None,
        project=None,
        log_store_name=None,
        dest_type=None,
        status=None,
        order_by=None,
        order=None,
        page_no=None,
        page_size=None,
    ):
        """
        Initialize ListLogShipperRequest request entity.

        :param log_shipper_id: log_shipper_id parameter
        :type log_shipper_id: str (optional)

        :param log_shipper_name: log_shipper_name parameter
        :type log_shipper_name: str (optional)

        :param project: project parameter
        :type project: str (optional)

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (optional)

        :param dest_type: dest_type parameter
        :type dest_type: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.log_shipper_id = log_shipper_id
        self.log_shipper_name = log_shipper_name
        self.project = project
        self.log_store_name = log_store_name
        self.dest_type = dest_type
        self.status = status
        self.order_by = order_by
        self.order = order
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
        :rtype: ListLogShipperRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logShipperID') is not None:
            self.log_shipper_id = m.get('logShipperID')
        if m.get('logShipperName') is not None:
            self.log_shipper_name = m.get('logShipperName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('destType') is not None:
            self.dest_type = m.get('destType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
