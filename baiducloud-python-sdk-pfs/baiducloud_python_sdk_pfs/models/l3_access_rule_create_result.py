"""
L3AccessRuleCreateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class L3AccessRuleCreateResult(AbstractModel):
    """
    L3AccessRuleCreateResult, 批量创建规则时的逐条结果
    """

    def __init__(self, success=None, access_rule_id=None, error_msg=None, ip=None, mask=None):
        """
        Initialize L3AccessRuleCreateResult instance.

        :param success: 该条规则是否创建成功
        :type success: bool (optional)

        :param access_rule_id: 创建成功时返回的规则 ID
        :type access_rule_id: int (optional)

        :param error_msg: 创建失败时的错误信息
        :type error_msg: str (optional)

        :param ip: 授权地址
        :type ip: str (optional)

        :param mask: 掩码位数
        :type mask: int (optional)
        """
        super().__init__()
        self.success = success
        self.access_rule_id = access_rule_id
        self.error_msg = error_msg
        self.ip = ip
        self.mask = mask

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
        if self.success is not None:
            result['success'] = self.success
        if self.access_rule_id is not None:
            result['accessRuleId'] = self.access_rule_id
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.ip is not None:
            result['ip'] = self.ip
        if self.mask is not None:
            result['mask'] = self.mask
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: L3AccessRuleCreateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('accessRuleId') is not None:
            self.access_rule_id = m.get('accessRuleId')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('mask') is not None:
            self.mask = m.get('mask')
        return self
