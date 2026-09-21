"""
LoggingService information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LoggingService(AbstractModel):
    """
    LoggingService
    """

    def __init__(self, enabled=None, log_type=None, status=None, supported=None):
        """
        Initialize LoggingService instance.

        :param enabled:
        :type enabled: bool (optional)

        :param log_type:
        :type log_type: str (optional)

        :param status:
        :type status: str (optional)

        :param supported:
        :type supported: bool (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.log_type = log_type
        self.status = status
        self.supported = supported

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
        if self.log_type is not None:
            result['logType'] = self.log_type
        if self.status is not None:
            result['status'] = self.status
        if self.supported is not None:
            result['supported'] = self.supported
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LoggingService

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('logType') is not None:
            self.log_type = m.get('logType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('supported') is not None:
            self.supported = m.get('supported')
        return self
