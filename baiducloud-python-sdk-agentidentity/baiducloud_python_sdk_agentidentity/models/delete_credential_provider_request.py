"""
Request entity for DeleteCredentialProviderRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteCredentialProviderRequest(AbstractModel):
    """
    Request entity for DeleteCredentialProviderRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, credential_provider_id):
        """
        Initialize DeleteCredentialProviderRequest request entity.

        :param credential_provider_id: 凭证提供方 ID
        :type credential_provider_id: str (required)
        """
        super().__init__()
        self.credential_provider_id = credential_provider_id

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
        if self.credential_provider_id is not None:
            result['credentialProviderId'] = self.credential_provider_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteCredentialProviderRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('credentialProviderId') is not None:
            self.credential_provider_id = m.get('credentialProviderId')
        return self
