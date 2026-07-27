"""
Request entity for GetTaskDetailV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetTaskDetailV2Request(AbstractModel):
    """
    Request entity for GetTaskDetailV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, dag_id, task_id, ignore_children=None, locale=None):
        """
        Initialize GetTaskDetailV2Request request entity.

        :param dag_id: dag_id parameter
        :type dag_id: str (required)

        :param task_id: task_id parameter
        :type task_id: str (required)

        :param ignore_children: ignore_children parameter
        :type ignore_children: str (optional)

        :param locale: locale parameter
        :type locale: str (optional)
        """
        super().__init__()
        self.dag_id = dag_id
        self.task_id = task_id
        self.ignore_children = ignore_children
        self.locale = locale

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTaskDetailV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dagId') is not None:
            self.dag_id = m.get('dagId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('ignoreChildren') is not None:
            self.ignore_children = m.get('ignoreChildren')
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
