"""
Request entity for ListTaskResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.task_detail import TaskDetail


class ListTaskResponse(BceResponse):
    """
    ListTaskResponse
    """

    def __init__(self, is_truncated=None, marker=None, max_keys=None, next_marker=None, tasks=None):
        """
        Initialize ListTaskResponse response.

        :param is_truncated: 是否截断
        :type is_truncated: bool (optional)

        :param marker: 当前页标记
        :type marker: str (optional)

        :param max_keys: 每页最大数量
        :type max_keys: int (optional)

        :param next_marker: 下一页标记
        :type next_marker: str (optional)

        :param tasks: 任务详情列表
        :type tasks: List[TaskDetail] (optional)
        """
        super().__init__()
        self.is_truncated = is_truncated
        self.marker = marker
        self.max_keys = max_keys
        self.next_marker = next_marker
        self.tasks = tasks

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
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.tasks is not None:
            result['tasks'] = [i.to_dict() for i in self.tasks]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListTaskResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('tasks') is not None:
            self.tasks = [TaskDetail().from_dict(i) for i in m.get('tasks')]
        return self
