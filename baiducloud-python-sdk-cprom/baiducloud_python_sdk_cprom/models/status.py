"""
Status information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Status(AbstractModel):
    """
    Status
    """

    def __init__(self, phase=None, ready=None, message=None):
        """
        Initialize Status instance.

        :param phase: 监控实例状态，可选值：Pending, Creating, Failed, Running, Upgrading
        :type phase: str (optional)

        :param ready: 监控实例是否ready
        :type ready: bool (optional)

        :param message: 监控实例状态说明信息
        :type message: str (optional)
        """
        super().__init__()
        self.phase = phase
        self.ready = ready
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
        if self.phase is not None:
            result['phase'] = self.phase
        if self.ready is not None:
            result['ready'] = self.ready
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
        :rtype: Status

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('ready') is not None:
            self.ready = m.get('ready')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
