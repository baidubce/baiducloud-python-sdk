"""
Request entity for QueryTaskListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.task import Task


class QueryTaskListResponse(BceResponse):
    """
    QueryTaskListResponse
    """

    def __init__(self, tasks=None, count=None):
        """
        Initialize QueryTaskListResponse response.

        :param tasks: 任务列表，元素结构见下方 Task
        :type tasks: List[Task] (optional)

        :param count: 符合查询条件的任务总数
        :type count: int (optional)
        """
        super().__init__()
        self.tasks = tasks
        self.count = count

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.tasks is not None:
            result['tasks'] = [i.to_dict() for i in self.tasks]
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryTaskListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = [Task().from_dict(i) for i in m.get('tasks')]
        if m.get('count') is not None:
            self.count = m.get('count')
        return self
