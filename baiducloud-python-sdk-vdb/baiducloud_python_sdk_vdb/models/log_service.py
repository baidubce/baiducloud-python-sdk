"""
LogService information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogService(AbstractModel):
    """
    LogService
    """

    def __init__(self, enabled=None, log_store_name=None, project=None, retention_days=None):
        """
        Initialize LogService instance.

        :param enabled:
        :type enabled: bool (optional)

        :param log_store_name:
        :type log_store_name: str (optional)

        :param project:
        :type project: str (optional)

        :param retention_days:
        :type retention_days: int (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.log_store_name = log_store_name
        self.project = project
        self.retention_days = retention_days

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.project is not None:
            result['project'] = self.project
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogService

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        return self
