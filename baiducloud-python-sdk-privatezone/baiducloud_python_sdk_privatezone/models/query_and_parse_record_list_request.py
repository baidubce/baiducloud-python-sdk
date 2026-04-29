"""
Request entity for QueryAndParseRecordListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryAndParseRecordListRequest(AbstractModel):
    """
    Request entity for QueryAndParseRecordListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, zone_id, marker=None, max_keys=None, rr=None, search_mode=None, type=None, value=None):
        """
        Initialize QueryAndParseRecordListRequest request entity.

        :param zone_id: zone_id parameter
        :type zone_id: str (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param rr: rr parameter
        :type rr: str (optional)

        :param search_mode: search_mode parameter
        :type search_mode: str (optional)

        :param type: type parameter
        :type type: str (optional)

        :param value: value parameter
        :type value: str (optional)
        """
        super().__init__()
        self.zone_id = zone_id
        self.marker = marker
        self.max_keys = max_keys
        self.rr = rr
        self.search_mode = search_mode
        self.type = type
        self.value = value

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
        :rtype: QueryAndParseRecordListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('rr') is not None:
            self.rr = m.get('rr')
        if m.get('searchMode') is not None:
            self.search_mode = m.get('searchMode')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
