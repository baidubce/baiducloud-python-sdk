"""
UpdateEncryptPolicyRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.encrypt_policy_request import EncryptPolicyRequest


class UpdateEncryptPolicyRequest(AbstractModel):
    """
    UpdateEncryptPolicyRequest
    """

    def __init__(self, encrypt_strategy=None):
        """
        Initialize UpdateEncryptPolicyRequest instance.

        :param encrypt_strategy: 加密策略配置
        :type encrypt_strategy: List[EncryptPolicyRequest] (optional)
        """
        super().__init__()
        self.encrypt_strategy = encrypt_strategy

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
        if self.encrypt_strategy is not None:
            result['encryptStrategy'] = [i.to_dict() for i in self.encrypt_strategy]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateEncryptPolicyRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('encryptStrategy') is not None:
            self.encrypt_strategy = [EncryptPolicyRequest().from_dict(i) for i in m.get('encryptStrategy')]
        return self
