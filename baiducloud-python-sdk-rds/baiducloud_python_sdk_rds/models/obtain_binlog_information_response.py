"""
Request entity for ObtainBinlogInformationResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.binlog import Binlog


class ObtainBinlogInformationResponse(BceResponse):
    """
    ObtainBinlogInformationResponse
    """

    def __init__(self, binlog=None):
        """
        Initialize ObtainBinlogInformationResponse response.

        :param binlog: binlog field
        :type binlog: Binlog (optional)
        """
        super().__init__()
        self.binlog = binlog

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.binlog is not None:
            result['binlog'] = self.binlog.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObtainBinlogInformationResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('binlog') is not None:
            self.binlog = Binlog().from_dict(m.get('binlog'))
        return self
