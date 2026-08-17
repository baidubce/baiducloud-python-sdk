"""
CredentialOp information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CredentialOp(AbstractModel):
    """
    CredentialOp
    """

    def __init__(self, operation=None, credential_name=None, value=None):
        """
        Initialize CredentialOp instance.

        :param operation: add、delete 或 rotate
        :type operation: str (optional)

        :param credential_name: 凭证名称
        :type credential_name: str (optional)

        :param value: 凭证值
        :type value: str (optional)
        """
        super().__init__()
        self.operation = operation
        self.credential_name = credential_name
        self.value = value

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.operation is not None:
            result['operation'] = self.operation
        if self.credential_name is not None:
            result['credentialName'] = self.credential_name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CredentialOp

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
