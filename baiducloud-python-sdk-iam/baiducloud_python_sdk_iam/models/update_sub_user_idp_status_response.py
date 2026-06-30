"""
Request entity for UpdateSubUserIdpStatusResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.idp import Idp


class UpdateSubUserIdpStatusResponse(BceResponse):
    """
    UpdateSubUserIdpStatusResponse
    """

    def __init__(self, idp=None):
        """
        Initialize UpdateSubUserIdpStatusResponse response.

        :param idp: idp field
        :type idp: Idp (optional)
        """
        super().__init__()
        self.idp = idp

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
        if self.idp is not None:
            result['idp'] = self.idp.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateSubUserIdpStatusResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('idp') is not None:
            self.idp = Idp().from_dict(m.get('idp'))
        return self
