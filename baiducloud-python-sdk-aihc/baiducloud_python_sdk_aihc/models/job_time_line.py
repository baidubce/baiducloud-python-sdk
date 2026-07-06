"""
JobTimeLine information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class JobTimeLine(AbstractModel):
    """
    JobTimeLine
    """

    def __init__(self, condition_type=None, condition_message=None, time=None):
        """
        Initialize JobTimeLine instance.

        :param condition_type: condition_type attribute
        :type condition_type: str (optional)

        :param condition_message: condition_message attribute
        :type condition_message: str (optional)

        :param time: 任务进入当前状态的时间（如 2024-05-20T14:30:00+08:00）
        :type time: str (optional)
        """
        super().__init__()
        self.condition_type = condition_type
        self.condition_message = condition_message
        self.time = time

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
        if self.condition_type is not None:
            result['conditionType'] = self.condition_type
        if self.condition_message is not None:
            result['conditionMessage'] = self.condition_message
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: JobTimeLine

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('conditionType') is not None:
            self.condition_type = m.get('conditionType')
        if m.get('conditionMessage') is not None:
            self.condition_message = m.get('conditionMessage')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self
