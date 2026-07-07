"""
Request entity for UpdateCredentialProviderRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateCredentialProviderRequest(AbstractModel):
    """
    Request entity for UpdateCredentialProviderRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, credential_provider_id, desc=None, credential=None):
        """
        Initialize UpdateCredentialProviderRequest request entity.

        :param credential_provider_id: 凭证提供方 ID
        :type credential_provider_id: str (required)

        :param desc: 新的描述，最多 128 字符
        :type desc: str (optional)

        :param credential: 新的凭证内容（与 desc 至少提供一个）
        :type credential: object (optional)
        """
        super().__init__()
        self.credential_provider_id = credential_provider_id
        self.desc = desc
        self.credential = credential

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
        if self.desc is not None:
            result['desc'] = self.desc
        if self.credential is not None:
            result['credential'] = self.credential
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateCredentialProviderRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('credentialProviderId') is not None:
            self.credential_provider_id = m.get('credentialProviderId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('credential') is not None:
            self.credential = m.get('credential')
        return self
