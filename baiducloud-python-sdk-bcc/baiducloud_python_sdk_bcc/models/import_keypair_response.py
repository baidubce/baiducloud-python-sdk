"""
Request entity for ImportKeypairResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.keypair_model import KeypairModel


class ImportKeypairResponse(BceResponse):
    """
    ImportKeypairResponse
    """

    def __init__(self, keypair=None):
        """
        Initialize ImportKeypairResponse response.

        :param keypair: keypair field
        :type keypair: KeypairModel (optional)
        """
        super().__init__()
        self.keypair = keypair

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
        if self.keypair is not None:
            result['keypair'] = self.keypair.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImportKeypairResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keypair') is not None:
            self.keypair = KeypairModel().from_dict(m.get('keypair'))
        return self
