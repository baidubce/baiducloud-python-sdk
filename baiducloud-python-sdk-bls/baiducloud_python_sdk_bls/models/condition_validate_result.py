"""
ConditionValidateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ConditionValidateResult(AbstractModel):
    """
    ConditionValidateResult
    """

    def __init__(self, valid=None, message=None):
        """
        Initialize ConditionValidateResult instance.

        :param valid: 是否通过验证
        :type valid: bool (optional)

        :param message: 验证失败时的错误信息
        :type message: str (optional)
        """
        super().__init__()
        self.valid = valid
        self.message = message

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
        if self.valid is not None:
            result['valid'] = self.valid
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConditionValidateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
