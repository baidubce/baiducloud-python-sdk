"""
Request entity for LogListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogListRequest(AbstractModel):
    """
    Request entity for LogListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, file_type, start_time, end_time=None):
        """
        Initialize LogListRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param file_type: file_type parameter
        :type file_type: str (required)

        :param start_time: start_time parameter
        :type start_time: str (required)

        :param end_time: end_time parameter
        :type end_time: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.file_type = file_type
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
