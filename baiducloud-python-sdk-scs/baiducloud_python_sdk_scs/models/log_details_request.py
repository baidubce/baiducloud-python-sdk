"""
Request entity for LogDetailsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogDetailsRequest(AbstractModel):
    """
    Request entity for LogDetailsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, log_id, valid_seconds=None):
        """
        Initialize LogDetailsRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param log_id: log_id parameter
        :type log_id: str (required)

        :param valid_seconds: valid_seconds parameter
        :type valid_seconds: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.log_id = log_id
        self.valid_seconds = valid_seconds

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
        :rtype: LogDetailsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('logId') is not None:
            self.log_id = m.get('logId')
        if m.get('validSeconds') is not None:
            self.valid_seconds = m.get('validSeconds')
        return self
