"""
DownloadTaskResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.task import Task


class DownloadTaskResult(AbstractModel):
    """
    DownloadTaskResult
    """

    def __init__(self, task=None):
        """
        Initialize DownloadTaskResult instance.

        :param task: task attribute
        :type task: Task (optional)
        """
        super().__init__()
        self.task = task

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
        if self.task is not None:
            result['task'] = self.task.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DownloadTaskResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task') is not None:
            self.task = Task().from_dict(m.get('task'))
        return self
