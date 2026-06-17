"""
LogStoreBatchRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogStoreBatchRequest(AbstractModel):
    """
    LogStoreBatchRequest
    """

    def __init__(self, project=None, log_store_name=None):
        """
        Initialize LogStoreBatchRequest instance.

        :param project: 项目名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)
        """
        super().__init__()
        self.project = project
        self.log_store_name = log_store_name

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
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogStoreBatchRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        return self
