"""
Request entity for GetMysqlSlowLogTimeDistributionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetMysqlSlowLogTimeDistributionRequest(AbstractModel):
    """
    Request entity for GetMysqlSlowLogTimeDistributionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, start, end, node_id=None, db_names=None, fingerprint_md5=None):
        """
        Initialize GetMysqlSlowLogTimeDistributionRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)

        :param node_id: node_id parameter
        :type node_id: str (optional)

        :param start: start parameter
        :type start: datetime (required)

        :param end: end parameter
        :type end: datetime (required)

        :param db_names: db_names parameter
        :type db_names: str (optional)

        :param fingerprint_md5: fingerprint_md5 parameter
        :type fingerprint_md5: str (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.node_id = node_id
        self.start = start
        self.end = end
        self.db_names = db_names
        self.fingerprint_md5 = fingerprint_md5

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
        :rtype: GetMysqlSlowLogTimeDistributionRequest

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
        if m.get('dbNames') is not None:
            self.db_names = m.get('dbNames')
        if m.get('fingerprintMd5') is not None:
            self.fingerprint_md5 = m.get('fingerprintMd5')
        return self
