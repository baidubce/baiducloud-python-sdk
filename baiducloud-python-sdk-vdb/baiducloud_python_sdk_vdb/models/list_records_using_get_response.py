"""
Request entity for ListRecordsUsingGETResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vdb.models.record import Record


class ListRecordsUsingGETResponse(BceResponse):
    """
    ListRecordsUsingGETResponse
    """

    def __init__(self, records=None, total=None):
        """
        Initialize ListRecordsUsingGETResponse response.

        :param records: records field
        :type records: List[Record] (optional)

        :param total: total field
        :type total: int (optional)
        """
        super().__init__()
        self.records = records
        self.total = total

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
        if self.records is not None:
            result['records'] = [i.to_dict() for i in self.records]
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListRecordsUsingGETResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('records') is not None:
            self.records = [Record().from_dict(i) for i in m.get('records')]
        if m.get('total') is not None:
            self.total = m.get('total')
        return self
