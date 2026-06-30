"""
Request entity for ModifySubUserOperationProtectionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifySubUserOperationProtectionRequest(AbstractModel):
    """
    Request entity for ModifySubUserOperationProtectionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_name, enabled_mfa, mfa_type=None):
        """
        Initialize ModifySubUserOperationProtectionRequest request entity.

        :param user_name: 需要更新的子用户名称
        :type user_name: str (required)

        :param enabled_mfa: 开启或关闭子用户操作保护
        :type enabled_mfa: bool (required)

        :param mfa_type: 子用户操作保护类型
        :type mfa_type: str (optional)
        """
        super().__init__()
        self.user_name = user_name
        self.enabled_mfa = enabled_mfa
        self.mfa_type = mfa_type

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
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.enabled_mfa is not None:
            result['enabledMfa'] = self.enabled_mfa
        if self.mfa_type is not None:
            result['mfaType'] = self.mfa_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifySubUserOperationProtectionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('enabledMfa') is not None:
            self.enabled_mfa = m.get('enabledMfa')
        if m.get('mfaType') is not None:
            self.mfa_type = m.get('mfaType')
        return self
