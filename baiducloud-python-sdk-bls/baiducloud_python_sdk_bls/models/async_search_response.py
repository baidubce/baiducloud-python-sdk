"""
Request entity for AsyncSearchResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.response import Response
from baiducloud_python_sdk_bls.models.error import Error


class AsyncSearchResponse(BceResponse):
    """
    AsyncSearchResponse
    """

    def __init__(
        self, start_time_in_millis=None, expiration_time_in_millis=None, response=None, error=None, status=None
    ):
        """
        Initialize AsyncSearchResponse response.

        :param start_time_in_millis: 查询开始时间
        :type start_time_in_millis: int (optional)

        :param expiration_time_in_millis: 查询结束时间
        :type expiration_time_in_millis: int (optional)

        :param response: response field
        :type response: Response (optional)

        :param error: error field
        :type error: Error (optional)

        :param status: http状态码，比如：500
        :type status: int (optional)
        """
        super().__init__()
        self.start_time_in_millis = start_time_in_millis
        self.expiration_time_in_millis = expiration_time_in_millis
        self.response = response
        self.error = error
        self.status = status

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
        if self.start_time_in_millis is not None:
            result['start_time_in_millis'] = self.start_time_in_millis
        if self.expiration_time_in_millis is not None:
            result['expiration_time_in_millis'] = self.expiration_time_in_millis
        if self.response is not None:
            result['response'] = self.response.to_dict()
        if self.error is not None:
            result['error'] = self.error.to_dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AsyncSearchResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('start_time_in_millis') is not None:
            self.start_time_in_millis = m.get('start_time_in_millis')
        if m.get('expiration_time_in_millis') is not None:
            self.expiration_time_in_millis = m.get('expiration_time_in_millis')
        if m.get('response') is not None:
            self.response = Response().from_dict(m.get('response'))
        if m.get('error') is not None:
            self.error = Error().from_dict(m.get('error'))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
