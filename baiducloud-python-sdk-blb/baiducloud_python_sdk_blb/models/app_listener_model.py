"""
AppListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppListenerModel(AbstractModel):
    """
    AppListenerModel
    """

    def __init__(
        self,
        listener_port=None,
        listener_type=None,
        scheduler=None,
        tcp_session_timeout=None,
        udp_session_timeout=None,
        keep_session=None,
        keep_session_type=None,
        keep_session_timeout=None,
        keep_session_cookie_name=None,
        x_forward_for=None,
        x_forwarded_proto=None,
        server_timeout=None,
        redirect_port=None,
        cert_ids=None,
        dual_auth=None,
        client_cert_ids=None,
        encryption_type=None,
        encryption_protocols=None,
        applied_ciphers=None,
    ):
        """
        Initialize AppListenerModel instance.

        :param listener_port: 监听器的监听端口
        :type listener_port: int (optional)

        :param listener_type: 监听器的监听类型
        :type listener_type: str (optional)

        :param scheduler: scheduler attribute
        :type scheduler: str (optional)

        :param tcp_session_timeout: tcp设置连接超时时间（单位：秒）
        :type tcp_session_timeout: int (optional)

        :param udp_session_timeout: udp设置连接超时时间（单位：秒）
        :type udp_session_timeout: int (optional)

        :param keep_session: 是否开启会话保持功能，即同一个Client发出的请求都会到达同一个后端服务器
        :type keep_session: bool (optional)

        :param keep_session_type: 会话保持的cookie处理方式，当且仅当开启会话保持时有效
        :type keep_session_type: str (optional)

        :param keep_session_timeout: 会话保持的cookie有效时间（单位：秒），当且仅当开启会话保持时有效
        :type keep_session_timeout: int (optional)

        :param keep_session_cookie_name: 会话保持需要覆盖的cookie名称，当且仅当开启会话保持且keepSessionType=\"rewrite\"时有效
        :type keep_session_cookie_name: str (optional)

        :param x_forward_for: x_forward_for attribute
        :type x_forward_for: bool (optional)

        :param x_forwarded_proto: x_forwarded_proto attribute
        :type x_forwarded_proto: bool (optional)

        :param server_timeout: 后端服务器最大超时时间（单位：秒）
        :type server_timeout: int (optional)

        :param redirect_port: 将此监听器收到的请求转发到HTTPS监听器，HTTPS监听器通过这个端口指定
        :type redirect_port: int (optional)

        :param cert_ids: 加载的SSl证书，目前HTTPS监听器只能绑定一个SSL证书
        :type cert_ids: List[str] (optional)

        :param dual_auth: 是否开启双向认证，默认为关闭
        :type dual_auth: bool (optional)

        :param client_cert_ids: 当dualAuth为true时，加载的客户端证书链
        :type client_cert_ids: List[str] (optional)

        :param encryption_type: 加密类型
        :type encryption_type: str (optional)

        :param encryption_protocols: 加密协议
        :type encryption_protocols: List[str] (optional)

        :param applied_ciphers: 加密套件
        :type applied_ciphers: str (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.listener_type = listener_type
        self.scheduler = scheduler
        self.tcp_session_timeout = tcp_session_timeout
        self.udp_session_timeout = udp_session_timeout
        self.keep_session = keep_session
        self.keep_session_type = keep_session_type
        self.keep_session_timeout = keep_session_timeout
        self.keep_session_cookie_name = keep_session_cookie_name
        self.x_forward_for = x_forward_for
        self.x_forwarded_proto = x_forwarded_proto
        self.server_timeout = server_timeout
        self.redirect_port = redirect_port
        self.cert_ids = cert_ids
        self.dual_auth = dual_auth
        self.client_cert_ids = client_cert_ids
        self.encryption_type = encryption_type
        self.encryption_protocols = encryption_protocols
        self.applied_ciphers = applied_ciphers

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
        if self.listener_type is not None:
            result['listenerType'] = self.listener_type
        if self.scheduler is not None:
            result['scheduler'] = self.scheduler
        if self.tcp_session_timeout is not None:
            result['tcpSessionTimeout'] = self.tcp_session_timeout
        if self.udp_session_timeout is not None:
            result['udpSessionTimeout'] = self.udp_session_timeout
        if self.keep_session is not None:
            result['keepSession'] = self.keep_session
        if self.keep_session_type is not None:
            result['keepSessionType'] = self.keep_session_type
        if self.keep_session_timeout is not None:
            result['keepSessionTimeout'] = self.keep_session_timeout
        if self.keep_session_cookie_name is not None:
            result['keepSessionCookieName'] = self.keep_session_cookie_name
        if self.x_forward_for is not None:
            result['xForwardFor'] = self.x_forward_for
        if self.x_forwarded_proto is not None:
            result['xForwardedProto'] = self.x_forwarded_proto
        if self.server_timeout is not None:
            result['serverTimeout'] = self.server_timeout
        if self.redirect_port is not None:
            result['redirectPort'] = self.redirect_port
        if self.cert_ids is not None:
            result['certIds'] = self.cert_ids
        if self.dual_auth is not None:
            result['dualAuth'] = self.dual_auth
        if self.client_cert_ids is not None:
            result['clientCertIds'] = self.client_cert_ids
        if self.encryption_type is not None:
            result['encryptionType'] = self.encryption_type
        if self.encryption_protocols is not None:
            result['encryptionProtocols'] = self.encryption_protocols
        if self.applied_ciphers is not None:
            result['appliedCiphers'] = self.applied_ciphers
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppListenerModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('listenerType') is not None:
            self.listener_type = m.get('listenerType')
        if m.get('scheduler') is not None:
            self.scheduler = m.get('scheduler')
        if m.get('tcpSessionTimeout') is not None:
            self.tcp_session_timeout = m.get('tcpSessionTimeout')
        if m.get('udpSessionTimeout') is not None:
            self.udp_session_timeout = m.get('udpSessionTimeout')
        if m.get('keepSession') is not None:
            self.keep_session = m.get('keepSession')
        if m.get('keepSessionType') is not None:
            self.keep_session_type = m.get('keepSessionType')
        if m.get('keepSessionTimeout') is not None:
            self.keep_session_timeout = m.get('keepSessionTimeout')
        if m.get('keepSessionCookieName') is not None:
            self.keep_session_cookie_name = m.get('keepSessionCookieName')
        if m.get('xForwardFor') is not None:
            self.x_forward_for = m.get('xForwardFor')
        if m.get('xForwardedProto') is not None:
            self.x_forwarded_proto = m.get('xForwardedProto')
        if m.get('serverTimeout') is not None:
            self.server_timeout = m.get('serverTimeout')
        if m.get('redirectPort') is not None:
            self.redirect_port = m.get('redirectPort')
        if m.get('certIds') is not None:
            self.cert_ids = m.get('certIds')
        if m.get('dualAuth') is not None:
            self.dual_auth = m.get('dualAuth')
        if m.get('clientCertIds') is not None:
            self.client_cert_ids = m.get('clientCertIds')
        if m.get('encryptionType') is not None:
            self.encryption_type = m.get('encryptionType')
        if m.get('encryptionProtocols') is not None:
            self.encryption_protocols = m.get('encryptionProtocols')
        if m.get('appliedCiphers') is not None:
            self.applied_ciphers = m.get('appliedCiphers')
        return self
