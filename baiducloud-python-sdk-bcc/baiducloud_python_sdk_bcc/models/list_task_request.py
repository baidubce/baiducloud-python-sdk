"""
Request entity for ListTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListTaskRequest(AbstractModel):
    """
    Request entity for ListTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        task_ids=None,
        marker=None,
        max_keys=None,
        task_action=None,
        task_status=None,
        start_time=None,
        end_time=None,
        resource_ids=None,
    ):
        """
        Initialize ListTaskRequest request entity.

        :param task_ids: 任务ID列表，最多100个。
        :type task_ids: List[str] (optional)

        :param marker: marker 任务ID
        :type marker: str (optional)

        :param max_keys: 默认值10，最大100。
        :type max_keys: int (optional)

        :param task_action: 取值范围：AttachDeploymentSets：调整部署集
        :type task_action: str (optional)

        :param task_status: task_status parameter
        :type task_status: str (optional)

        :param start_time: start_time parameter
        :type start_time: str (optional)

        :param end_time: end_time parameter
        :type end_time: str (optional)

        :param resource_ids: 资源ID。单次最多支持指定 100 个，当taskAction为调整部署集时为实例ID
        :type resource_ids: List[str] (optional)
        """
        super().__init__()
        self.task_ids = task_ids
        self.marker = marker
        self.max_keys = max_keys
        self.task_action = task_action
        self.task_status = task_status
        self.start_time = start_time
        self.end_time = end_time
        self.resource_ids = resource_ids

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
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        return self
