"""
AppSSLListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppSSLListenerModel(AbstractModel):
    """
    AppSSLListenerModel
    """

    def __init__(
        self,
        listener_port=None,
        scheduler=None,
        cert_ids=None,
        encryption_type=None,
        encryption_protocols=None,
        applied_ciphers=None,
        dual_auth=None,
        client_cert_ids=None,
        description=None,
    ):
        """
        Initialize AppSSLListenerModel instance.

        :param listener_port: 监听器的监听端口
        :type listener_port: int (optional)

        :param scheduler: scheduler attribute
        :type scheduler: str (optional)

        :param cert_ids: 加载的SSl证书链
        :type cert_ids: List[str] (optional)

        :param encryption_type: 加密类型
        :type encryption_type: str (optional)

        :param encryption_protocols: 加密协议
        :type encryption_protocols: List[str] (optional)

        :param applied_ciphers: 加密套件
        :type applied_ciphers: str (optional)

        :param dual_auth: 是否开启双向认证，默认为关闭
        :type dual_auth: bool (optional)

        :param client_cert_ids: 当dualAuth为true时，加载的客户端证书链
        :type client_cert_ids: List[str] (optional)

        :param description: 描述信息，长度不超过200个字符。
        :type description: str (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.scheduler = scheduler
        self.cert_ids = cert_ids
        self.encryption_type = encryption_type
        self.encryption_protocols = encryption_protocols
        self.applied_ciphers = applied_ciphers
        self.dual_auth = dual_auth
        self.client_cert_ids = client_cert_ids
        self.description = description

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
        if self.listener_port is not None:
            result['listenerPort'] = self.listener_port
        if self.scheduler is not None:
            result['scheduler'] = self.scheduler
        if self.cert_ids is not None:
            result['certIds'] = self.cert_ids
        if self.encryption_type is not None:
            result['encryptionType'] = self.encryption_type
        if self.encryption_protocols is not None:
            result['encryptionProtocols'] = self.encryption_protocols
        if self.applied_ciphers is not None:
            result['appliedCiphers'] = self.applied_ciphers
        if self.dual_auth is not None:
            result['dualAuth'] = self.dual_auth
        if self.client_cert_ids is not None:
            result['clientCertIds'] = self.client_cert_ids
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppSSLListenerModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('scheduler') is not None:
            self.scheduler = m.get('scheduler')
        if m.get('certIds') is not None:
            self.cert_ids = m.get('certIds')
        if m.get('encryptionType') is not None:
            self.encryption_type = m.get('encryptionType')
        if m.get('encryptionProtocols') is not None:
            self.encryption_protocols = m.get('encryptionProtocols')
        if m.get('appliedCiphers') is not None:
            self.applied_ciphers = m.get('appliedCiphers')
        if m.get('dualAuth') is not None:
            self.dual_auth = m.get('dualAuth')
        if m.get('clientCertIds') is not None:
            self.client_cert_ids = m.get('clientCertIds')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
