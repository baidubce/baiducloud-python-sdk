"""
TaskResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TaskResult(AbstractModel):
    """
    TaskResult
    """

    def __init__(
        self,
        dest_resource=None,
        end_time=None,
        execution_id=None,
        id=None,
        job_id=None,
        operation=None,
        resource_type=None,
        src_resource=None,
        start_time=None,
        status=None,
    ):
        """
        Initialize TaskResult instance.

        :param dest_resource: 同步目标
        :type dest_resource: str (optional)

        :param end_time: 结束时间
        :type end_time: str (optional)

        :param execution_id: 任务执行结果所属的任务 ID
        :type execution_id: int (optional)

        :param id: 任务执行结果 ID
        :type id: int (optional)

        :param job_id: 与任务相关的基础作业 ID
        :type job_id: str (optional)

        :param operation: 任务的操作
        :type operation: str (optional)

        :param resource_type: 同步类型
        :type resource_type: str (optional)

        :param src_resource: 同步源
        :type src_resource: str (optional)

        :param start_time: 开始时间
        :type start_time: str (optional)

        :param status: 状态
        :type status: str (optional)
        """
        super().__init__()
        self.dest_resource = dest_resource
        self.end_time = end_time
        self.execution_id = execution_id
        self.id = id
        self.job_id = job_id
        self.operation = operation
        self.resource_type = resource_type
        self.src_resource = src_resource
        self.start_time = start_time
        self.status = status

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
        if self.dest_resource is not None:
            result['destResource'] = self.dest_resource
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_id is not None:
            result['executionId'] = self.execution_id
        if self.id is not None:
            result['id'] = self.id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.operation is not None:
            result['operation'] = self.operation
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.src_resource is not None:
            result['srcResource'] = self.src_resource
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TaskResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('destResource') is not None:
            self.dest_resource = m.get('destResource')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('srcResource') is not None:
            self.src_resource = m.get('srcResource')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
