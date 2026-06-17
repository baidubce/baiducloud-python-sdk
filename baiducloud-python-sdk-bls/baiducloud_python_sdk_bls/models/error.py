"""
Error information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Error(AbstractModel):
    """
    Error
    """

    def __init__(self, root_cause=None, type=None, reason=None):
        """
        Initialize Error instance.

        :param root_cause: 根原因
        :type root_cause: List[Error] (optional)

        :param type: 错误类型
        :type type: str (optional)

        :param reason: 错误原因
        :type reason: str (optional)
        """
        super().__init__()
        self.root_cause = root_cause
        self.type = type
        self.reason = reason

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
        if self.root_cause is not None:
            result['root_cause'] = [i.to_dict() for i in self.root_cause]
        if self.type is not None:
            result['type'] = self.type
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Error

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('root_cause') is not None:
            self.root_cause = [Error().from_dict(i) for i in m.get('root_cause')]
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self
