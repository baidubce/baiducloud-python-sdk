"""
Request entity for GetTLSInfoUsingGETResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetTLSInfoUsingGETResponse(BceResponse):
    """
    GetTLSInfoUsingGETResponse
    """

    def __init__(self, tls_expired_date=None, tls_issued_date=None, tls_status=None, tls_valid_days=None):
        """
        Initialize GetTLSInfoUsingGETResponse response.

        :param tls_expired_date: tls_expired_date field
        :type tls_expired_date: str (optional)

        :param tls_issued_date: tls_issued_date field
        :type tls_issued_date: str (optional)

        :param tls_status: tls_status field
        :type tls_status: str (optional)

        :param tls_valid_days: tls_valid_days field
        :type tls_valid_days: int (optional)
        """
        super().__init__()
        self.tls_expired_date = tls_expired_date
        self.tls_issued_date = tls_issued_date
        self.tls_status = tls_status
        self.tls_valid_days = tls_valid_days

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
            result['metadata'] = dict(self.metadata)
        if self.tls_expired_date is not None:
            result['tlsExpiredDate'] = self.tls_expired_date
        if self.tls_issued_date is not None:
            result['tlsIssuedDate'] = self.tls_issued_date
        if self.tls_status is not None:
            result['tlsStatus'] = self.tls_status
        if self.tls_valid_days is not None:
            result['tlsValidDays'] = self.tls_valid_days
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTLSInfoUsingGETResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tlsExpiredDate') is not None:
            self.tls_expired_date = m.get('tlsExpiredDate')
        if m.get('tlsIssuedDate') is not None:
            self.tls_issued_date = m.get('tlsIssuedDate')
        if m.get('tlsStatus') is not None:
            self.tls_status = m.get('tlsStatus')
        if m.get('tlsValidDays') is not None:
            self.tls_valid_days = m.get('tlsValidDays')
        return self
