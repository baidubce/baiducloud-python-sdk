"""
Request entity for SlowLogListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.openapi_slowlog import OpenapiSlowlog


class SlowLogListResponse(BceResponse):
    """
    SlowLogListResponse
    """

    def __init__(self, slowlogs=None):
        """
        Initialize SlowLogListResponse response.

        :param slowlogs: 慢日志下载对象
        :type slowlogs: List[OpenapiSlowlog] (optional)
        """
        super().__init__()
        self.slowlogs = slowlogs

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
        if self.slowlogs is not None:
            result['slowlogs'] = [i.to_dict() for i in self.slowlogs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SlowLogListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('slowlogs') is not None:
            self.slowlogs = [OpenapiSlowlog().from_dict(i) for i in m.get('slowlogs')]
        return self
