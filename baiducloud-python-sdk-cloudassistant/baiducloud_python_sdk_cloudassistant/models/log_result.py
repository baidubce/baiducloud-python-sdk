"""
LogResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.log import Log


class LogResult(AbstractModel):
    """
    LogResult
    """

    def __init__(self, logs=None, next_cursor=None, state=None, child_id=None):
        """
        Initialize LogResult instance.

        :param logs: 日志内容，顺序排列
        :type logs: List[Log] (optional)

        :param next_cursor: next_cursor attribute
        :type next_cursor: int (optional)

        :param state: state attribute
        :type state: str (optional)

        :param child_id: 子执行id
        :type child_id: str (optional)
        """
        super().__init__()
        self.logs = logs
        self.next_cursor = next_cursor
        self.state = state
        self.child_id = child_id

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
        if self.logs is not None:
            result['logs'] = [i.to_dict() for i in self.logs]
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        if self.state is not None:
            result['state'] = self.state
        if self.child_id is not None:
            result['childId'] = self.child_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logs') is not None:
            self.logs = [Log().from_dict(i) for i in m.get('logs')]
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('childId') is not None:
            self.child_id = m.get('childId')
        return self
