"""
TaskDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.operation_progress_set import OperationProgressSet


class TaskDetail(AbstractModel):
    """
    TaskDetail
    """

    def __init__(
        self,
        task_id=None,
        task_action=None,
        task_status=None,
        created_time=None,
        finished_time=None,
        total_count=None,
        success_count=None,
        failed_count=None,
        operation_progress_set=None,
    ):
        """
        Initialize TaskDetail instance.

        :param task_id: 任务ID
        :type task_id: str (optional)

        :param task_action: 任务类型
        :type task_action: str (optional)

        :param task_status: 任务状态：Processing 处理中，Finished 已完成，Failed 处理失败
        :type task_status: str (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param finished_time: 完成时间
        :type finished_time: str (optional)

        :param total_count: 总数
        :type total_count: int (optional)

        :param success_count: 成功数量
        :type success_count: int (optional)

        :param failed_count: 失败数量
        :type failed_count: int (optional)

        :param operation_progress_set: 操作列表，查询任务列表接口无此信息
        :type operation_progress_set: List[OperationProgressSet] (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.task_action = task_action
        self.task_status = task_status
        self.created_time = created_time
        self.finished_time = finished_time
        self.total_count = total_count
        self.success_count = success_count
        self.failed_count = failed_count
        self.operation_progress_set = operation_progress_set

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
            result['taskId'] = self.task_id
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.success_count is not None:
            result['successCount'] = self.success_count
        if self.failed_count is not None:
            result['failedCount'] = self.failed_count
        if self.operation_progress_set is not None:
            result['operationProgressSet'] = [i.to_dict() for i in self.operation_progress_set]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TaskDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')
        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')
        if m.get('operationProgressSet') is not None:
            self.operation_progress_set = [OperationProgressSet().from_dict(i) for i in m.get('operationProgressSet')]
        return self
