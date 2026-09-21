"""
Request entity for GetRedisBigKeyAnalysisResultResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.big_key_task import BigKeyTask


class GetRedisBigKeyAnalysisResultResponse(BceResponse):
    """
    GetRedisBigKeyAnalysisResultResponse
    """

    def __init__(self, tasks=None, total_count=None):
        """
        Initialize GetRedisBigKeyAnalysisResultResponse response.

        :param tasks: 任务列表
        :type tasks: List[BigKeyTask] (optional)

        :param total_count: 任务总个数
        :type total_count: int (optional)
        """
        super().__init__()
        self.tasks = tasks
        self.total_count = total_count

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetRedisBigKeyAnalysisResultResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = [BigKeyTask().from_dict(i) for i in m.get('tasks')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
