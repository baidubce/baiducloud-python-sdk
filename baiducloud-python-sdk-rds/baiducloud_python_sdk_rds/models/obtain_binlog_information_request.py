"""
Request entity for ObtainBinlogInformationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ObtainBinlogInformationRequest(AbstractModel):
    """
    Request entity for ObtainBinlogInformationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, log_id, download_valid_time_in_sec):
        """
        Initialize ObtainBinlogInformationRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param log_id: log_id parameter
        :type log_id: str (required)

        :param download_valid_time_in_sec: download_valid_time_in_sec parameter
        :type download_valid_time_in_sec: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.log_id = log_id
        self.download_valid_time_in_sec = download_valid_time_in_sec

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
        :rtype: ObtainBinlogInformationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('logId') is not None:
            self.log_id = m.get('logId')
        if m.get('downloadValidTimeInSec') is not None:
            self.download_valid_time_in_sec = m.get('downloadValidTimeInSec')
        return self
