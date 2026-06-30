"""
Request entity for UpdateLoginProfileRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateLoginProfileRequest(AbstractModel):
    """
    Request entity for UpdateLoginProfileRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        user_name,
        password=None,
        need_reset_password=None,
        enabled_login=None,
        enabled_login_mfa=None,
        login_mfa_type=None,
        third_party_type=None,
        third_party_account=None,
    ):
        """
        Initialize UpdateLoginProfileRequest request entity.

        :param user_name: user_name parameter
        :type user_name: str (required)

        :param password: 用户密码；作为响应时不显示
        :type password: str (optional)

        :param need_reset_password: 下次登录时是否需要重置密码
        :type need_reset_password: bool (optional)

        :param enabled_login: 是否允许子用户控制台登录
        :type enabled_login: bool (optional)

        :param enabled_login_mfa: 是否要求绑定二次验证设备
        :type enabled_login_mfa: bool (optional)

        :param login_mfa_type: 二次验证类型，可选：PHONE-手机号，TOTP虚拟MFA设备
        :type login_mfa_type: str (optional)

        :param third_party_type: 绑定的第三方登录类型，可选：UUAP-内网账号，PASSPORT-百度账号
        :type third_party_type: str (optional)

        :param third_party_account: 绑定的第三方登录账号。绑定类型为PASSPORT时可以是手机、邮箱以及账号名称
        :type third_party_account: str (optional)
        """
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.need_reset_password = need_reset_password
        self.enabled_login = enabled_login
        self.enabled_login_mfa = enabled_login_mfa
        self.login_mfa_type = login_mfa_type
        self.third_party_type = third_party_type
        self.third_party_account = third_party_account

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
        if self.password is not None:
            result['password'] = self.password
        if self.need_reset_password is not None:
            result['needResetPassword'] = self.need_reset_password
        if self.enabled_login is not None:
            result['enabledLogin'] = self.enabled_login
        if self.enabled_login_mfa is not None:
            result['enabledLoginMfa'] = self.enabled_login_mfa
        if self.login_mfa_type is not None:
            result['loginMfaType'] = self.login_mfa_type
        if self.third_party_type is not None:
            result['thirdPartyType'] = self.third_party_type
        if self.third_party_account is not None:
            result['thirdPartyAccount'] = self.third_party_account
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateLoginProfileRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('needResetPassword') is not None:
            self.need_reset_password = m.get('needResetPassword')
        if m.get('enabledLogin') is not None:
            self.enabled_login = m.get('enabledLogin')
        if m.get('enabledLoginMfa') is not None:
            self.enabled_login_mfa = m.get('enabledLoginMfa')
        if m.get('loginMfaType') is not None:
            self.login_mfa_type = m.get('loginMfaType')
        if m.get('thirdPartyType') is not None:
            self.third_party_type = m.get('thirdPartyType')
        if m.get('thirdPartyAccount') is not None:
            self.third_party_account = m.get('thirdPartyAccount')
        return self
