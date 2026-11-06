"""
EncryptPolicyRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EncryptPolicyRequest(AbstractModel):
    """
    EncryptPolicyRequest
    """

    def __init__(
        self, encrypt_enable=None, key_management_type=None, key_management_service_name=None, secret_key_id=None
    ):
        """
        Initialize EncryptPolicyRequest instance.

        :param encrypt_enable: 是否开启存储加密
        :type encrypt_enable: bool (optional)

        :param key_management_type: 密钥管理方式，自托管(self\\_kms)/百度KMS(baidu\\_kms)，当前仅支持self\\_kms
        :type key_management_type: str (optional)

        :param key_management_service_name: 密钥管理服务名称，当前为 rds
        :type key_management_service_name: str (optional)

        :param secret_key_id: 密钥ID
        :type secret_key_id: str (optional)
        """
        super().__init__()
        self.encrypt_enable = encrypt_enable
        self.key_management_type = key_management_type
        self.key_management_service_name = key_management_service_name
        self.secret_key_id = secret_key_id

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
        if self.encrypt_enable is not None:
            result['encryptEnable'] = self.encrypt_enable
        if self.key_management_type is not None:
            result['keyManagementType'] = self.key_management_type
        if self.key_management_service_name is not None:
            result['keyManagementServiceName'] = self.key_management_service_name
        if self.secret_key_id is not None:
            result['secretKeyID'] = self.secret_key_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EncryptPolicyRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('encryptEnable') is not None:
            self.encrypt_enable = m.get('encryptEnable')
        if m.get('keyManagementType') is not None:
            self.key_management_type = m.get('keyManagementType')
        if m.get('keyManagementServiceName') is not None:
            self.key_management_service_name = m.get('keyManagementServiceName')
        if m.get('secretKeyID') is not None:
            self.secret_key_id = m.get('secretKeyID')
        return self
