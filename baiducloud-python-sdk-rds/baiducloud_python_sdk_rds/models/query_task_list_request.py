"""
Request entity for QueryTaskListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryTaskListRequest(AbstractModel):
    """
    Request entity for QueryTaskListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_size=None,
        page_no=None,
        instance_id=None,
        instance_name=None,
        task_id=None,
        task_type=None,
        task_status=None,
        start_time=None,
        end_time=None,
    ):
        """
        Initialize QueryTaskListRequest request entity.

        :param page_size: 每页的大小
        :type page_size: str (optional)

        :param page_no: 页码
        :type page_no: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param task_id: 任务ID
        :type task_id: int (optional)

        :param task_type: 任务类型，可取值：resize/switch/reboot/changeAzone
        :type task_type: str (optional)

        :param task_status: 任务状态，可取值：created/running/success/failed/cancelled
        :type task_status: str (optional)

        :param start_time: 任务开始时间
        :type start_time: str (optional)

        :param end_time: 任务结束时间
        :type end_time: str (optional)
        """
        super().__init__()
        self.page_size = page_size
        self.page_no = page_no
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.task_id = task_id
        self.task_type = task_type
        self.task_status = task_status
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryTaskListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
