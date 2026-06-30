"""
ExecAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ExecAction(AbstractModel):
    """
    ExecAction
    """

    def __init__(self, command=None):
        """
        Initialize ExecAction instance.

        :param command: 容器内执行的健康检查命令
        :type command: List[str] (optional)
        """
        super().__init__()
        self.command = command

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
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExecAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        return self
