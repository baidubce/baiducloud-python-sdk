"""
SandboxResourceCondition information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SandboxResourceCondition(AbstractModel):
    """
    SandboxResourceCondition
    """

    def __init__(self, type=None, status=None, reason=None, message=None):
        """
        Initialize SandboxResourceCondition instance.

        :param type: 条件类型。
        :type type: str (optional)

        :param status: 条件状态。
        :type status: str (optional)

        :param reason: 原因。
        :type reason: str (optional)

        :param message: 详细信息。
        :type message: str (optional)
        """
        super().__init__()
        self.type = type
        self.status = status
        self.reason = reason
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
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.reason is not None:
            result['reason'] = self.reason
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
        :rtype: SandboxResourceCondition

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
