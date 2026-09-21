"""
Request entity for ListMysqlSlowLogsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListMysqlSlowLogsRequest(AbstractModel):
    """
    Request entity for ListMysqlSlowLogsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        app_id,
        start,
        end,
        node_id=None,
        users=None,
        db_names=None,
        client_ips=None,
        fingerprint_md5=None,
        order_by=None,
        order=None,
        page=None,
        page_size=None,
    ):
        """
        Initialize ListMysqlSlowLogsRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)

        :param node_id: node_id parameter
        :type node_id: str (optional)

        :param start: start parameter
        :type start: datetime (required)

        :param end: end parameter
        :type end: datetime (required)

        :param users: users parameter
        :type users: str (optional)

        :param db_names: db_names parameter
        :type db_names: str (optional)

        :param client_ips: client_ips parameter
        :type client_ips: str (optional)

        :param fingerprint_md5: fingerprint_md5 parameter
        :type fingerprint_md5: str (optional)

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
        self.start = start
        self.end = end
        self.users = users
        self.db_names = db_names
        self.client_ips = client_ips
        self.fingerprint_md5 = fingerprint_md5
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
        :rtype: ListMysqlSlowLogsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('users') is not None:
            self.users = m.get('users')
        if m.get('dbNames') is not None:
            self.db_names = m.get('dbNames')
        if m.get('clientIps') is not None:
            self.client_ips = m.get('clientIps')
        if m.get('fingerprintMd5') is not None:
            self.fingerprint_md5 = m.get('fingerprintMd5')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
