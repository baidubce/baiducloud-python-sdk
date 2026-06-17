"""
Request entity for TermsEnumResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.error import Error


class TermsEnumResponse(BceResponse):
    """
    TermsEnumResponse
    """

    def __init__(self, terms=None, error=None, status=None):
        """
        Initialize TermsEnumResponse response.

        :param terms: 返回匹配到的term值数组
        :type terms: List[str] (optional)

        :param error: error field
        :type error: Error (optional)

        :param status: http状态码，比如：500
        :type status: int (optional)
        """
        super().__init__()
        self.terms = terms
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
        if self.terms is not None:
            result['terms'] = self.terms
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
        :rtype: TermsEnumResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('terms') is not None:
            self.terms = m.get('terms')
        if m.get('error') is not None:
            self.error = Error().from_dict(m.get('error'))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
