"""
Request entity for GetTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetTaskRequest(AbstractModel):
    """
    Request entity for GetTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, task_ids, max_keys=None):
        """
        Initialize GetTaskRequest request entity.

        :param task_ids: 任务ID列表，最多100个。
        :type task_ids: List[str] (required)

        :param max_keys: 默认值100。
        :type max_keys: int (optional)
        """
        super().__init__()
        self.task_ids = task_ids
        self.max_keys = max_keys

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
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
