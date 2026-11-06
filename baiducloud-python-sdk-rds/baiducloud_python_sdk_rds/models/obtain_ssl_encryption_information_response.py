"""
Request entity for ObtainSslEncryptionInformationResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.ssl_state import SslState


class ObtainSslEncryptionInformationResponse(BceResponse):
    """
    ObtainSslEncryptionInformationResponse
    """

    def __init__(self, ssl_state=None):
        """
        Initialize ObtainSslEncryptionInformationResponse response.

        :param ssl_state: ssl_state field
        :type ssl_state: SslState (optional)
        """
        super().__init__()
        self.ssl_state = ssl_state

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
        if self.ssl_state is not None:
            result['sslState'] = self.ssl_state.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObtainSslEncryptionInformationResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sslState') is not None:
            self.ssl_state = SslState().from_dict(m.get('sslState'))
        return self
