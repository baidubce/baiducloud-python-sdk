"""
RetouchingCreateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RetouchingCreateResult(AbstractModel):
    """
    RetouchingCreateResult
    """

    def __init__(self, task_id=None, wait_task_count=None):
        """
        Initialize RetouchingCreateResult instance.

        :param task_id: 任务ID，用于查询任务结果，有效期8小时
        :type task_id: str (optional)

        :param wait_task_count: 排队等待的任务数量
        :type wait_task_count: int (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.wait_task_count = wait_task_count

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
        if self.task_id is not None:
            result['task_id'] = self.task_id
        if self.wait_task_count is not None:
            result['wait_task_count'] = self.wait_task_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RetouchingCreateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('wait_task_count') is not None:
            self.wait_task_count = m.get('wait_task_count')
        return self
