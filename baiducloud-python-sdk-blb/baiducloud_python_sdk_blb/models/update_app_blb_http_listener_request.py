"""
Request entity for UpdateAppBlbHttpListenerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.additional_attributes_model import AdditionalAttributesModel


class UpdateAppBlbHttpListenerRequest(AbstractModel):
    """
    Request entity for UpdateAppBlbHttpListenerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        blb_id,
        listener_port,
        scheduler,
        client_token=None,
        keep_session=None,
        keep_session_type=None,
        keep_session_timeout=None,
        keep_session_cookie_name=None,
        x_forwarded_for=None,
        x_forwarded_proto=None,
        additional_attributes=None,
        server_timeout=None,
        redirect_port=None,
        description=None,
    ):
        """
        Initialize UpdateAppBlbHttpListenerRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param listener_port: listener_port parameter
        :type listener_port: int (required)

        :param scheduler: scheduler parameter
        :type scheduler: str (required)

        :param keep_session: keep_session parameter
        :type keep_session: bool (optional)

        :param keep_session_type: keep_session_type parameter
        :type keep_session_type: str (optional)

        :param keep_session_timeout: keep_session_timeout parameter
        :type keep_session_timeout: int (optional)

        :param keep_session_cookie_name: 会话保持需要覆盖的cookie名称，当且仅当开启会话保持且keepSessionType=\"rewrite\"时有效
        :type keep_session_cookie_name: str (optional)

        :param x_forwarded_for: x_forwarded_for parameter
        :type x_forwarded_for: bool (optional)

        :param x_forwarded_proto: x_forwarded_proto parameter
        :type x_forwarded_proto: bool (optional)

        :param additional_attributes: additional_attributes parameter
        :type additional_attributes: AdditionalAttributesModel (optional)

        :param server_timeout: 后端服务器最大超时（单位：秒），默认30s，需为1-3600间的整数
        :type server_timeout: int (optional)

        :param redirect_port: 将此监听器收到的请求转发到HTTPS监听器，HTTPS监听器通过这个端口指定
        :type redirect_port: int (optional)

        :param description: 描述信息，长度不超过200个字符。
        :type description: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.listener_port = listener_port
        self.scheduler = scheduler
        self.keep_session = keep_session
        self.keep_session_type = keep_session_type
        self.keep_session_timeout = keep_session_timeout
        self.keep_session_cookie_name = keep_session_cookie_name
        self.x_forwarded_for = x_forwarded_for
        self.x_forwarded_proto = x_forwarded_proto
        self.additional_attributes = additional_attributes
        self.server_timeout = server_timeout
        self.redirect_port = redirect_port
        self.description = description

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
        if self.scheduler is not None:
            result['scheduler'] = self.scheduler
        if self.keep_session is not None:
            result['keepSession'] = self.keep_session
        if self.keep_session_type is not None:
            result['keepSessionType'] = self.keep_session_type
        if self.keep_session_timeout is not None:
            result['keepSessionTimeout'] = self.keep_session_timeout
        if self.keep_session_cookie_name is not None:
            result['keepSessionCookieName'] = self.keep_session_cookie_name
        if self.x_forwarded_for is not None:
            result['xForwardedFor'] = self.x_forwarded_for
        if self.x_forwarded_proto is not None:
            result['xForwardedProto'] = self.x_forwarded_proto
        if self.additional_attributes is not None:
            result['additionalAttributes'] = self.additional_attributes.to_dict()
        if self.server_timeout is not None:
            result['serverTimeout'] = self.server_timeout
        if self.redirect_port is not None:
            result['redirectPort'] = self.redirect_port
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAppBlbHttpListenerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('scheduler') is not None:
            self.scheduler = m.get('scheduler')
        if m.get('keepSession') is not None:
            self.keep_session = m.get('keepSession')
        if m.get('keepSessionType') is not None:
            self.keep_session_type = m.get('keepSessionType')
        if m.get('keepSessionTimeout') is not None:
            self.keep_session_timeout = m.get('keepSessionTimeout')
        if m.get('keepSessionCookieName') is not None:
            self.keep_session_cookie_name = m.get('keepSessionCookieName')
        if m.get('xForwardedFor') is not None:
            self.x_forwarded_for = m.get('xForwardedFor')
        if m.get('xForwardedProto') is not None:
            self.x_forwarded_proto = m.get('xForwardedProto')
        if m.get('additionalAttributes') is not None:
            self.additional_attributes = AdditionalAttributesModel().from_dict(m.get('additionalAttributes'))
        if m.get('serverTimeout') is not None:
            self.server_timeout = m.get('serverTimeout')
        if m.get('redirectPort') is not None:
            self.redirect_port = m.get('redirectPort')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
