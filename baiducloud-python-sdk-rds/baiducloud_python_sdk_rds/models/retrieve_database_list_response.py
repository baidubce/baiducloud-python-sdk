"""
Request entity for RetrieveDatabaseListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.database import Database


class RetrieveDatabaseListResponse(BceResponse):
    """
    RetrieveDatabaseListResponse
    """

    def __init__(self, databases=None):
        """
        Initialize RetrieveDatabaseListResponse response.

        :param databases: 由[Database](#Database)对象组成的数组。
        :type databases: List[Database] (optional)
        """
        super().__init__()
        self.databases = databases

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
        if self.databases is not None:
            result['databases'] = [i.to_dict() for i in self.databases]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RetrieveDatabaseListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('databases') is not None:
            self.databases = [Database().from_dict(i) for i in m.get('databases')]
        return self
