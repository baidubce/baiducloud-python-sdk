"""
Request entity for RetrieveTheBinlogListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.binlogs import Binlogs


class RetrieveTheBinlogListResponse(BceResponse):
    """
    RetrieveTheBinlogListResponse
    """

    def __init__(self, binlogs=None):
        """
        Initialize RetrieveTheBinlogListResponse response.

        :param binlogs: binlog 列表结果
        :type binlogs: List[Binlogs] (optional)
        """
        super().__init__()
        self.binlogs = binlogs

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
        if self.binlogs is not None:
            result['binlogs'] = [i.to_dict() for i in self.binlogs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RetrieveTheBinlogListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('binlogs') is not None:
            self.binlogs = [Binlogs().from_dict(i) for i in m.get('binlogs')]
        return self
