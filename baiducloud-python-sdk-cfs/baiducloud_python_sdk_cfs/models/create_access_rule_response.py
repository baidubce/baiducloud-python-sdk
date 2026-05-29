"""
CreateAccessRuleResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAccessRuleResponse(BceResponse):
    """
    CreateAccessRuleResponse
    """

    def __init__(self, sucess=None, ar_idx=None, err_msg=None):
        """
        Initialize CreateAccessRuleResponse instance.

        :param sucess: 表示对应的规则是否成功创建
        :type sucess: bool (optional)

        :param ar_idx: 如果创建成功，包含该字段表示成功创建的规则的标识符
        :type ar_idx: int (optional)

        :param err_msg: 如果创建失败，包含该字段表示该规则创建失败的原因
        :type err_msg: str (optional)
        """
        super().__init__()
        self.sucess = sucess
        self.ar_idx = ar_idx
        self.err_msg = err_msg

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.sucess is not None:
            result['sucess'] = self.sucess
        if self.ar_idx is not None:
            result['ar_idx'] = self.ar_idx
        if self.err_msg is not None:
            result['err_msg'] = self.err_msg
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAccessRuleResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sucess') is not None:
            self.sucess = m.get('sucess')
        if m.get('ar_idx') is not None:
            self.ar_idx = m.get('ar_idx')
        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')
        return self
