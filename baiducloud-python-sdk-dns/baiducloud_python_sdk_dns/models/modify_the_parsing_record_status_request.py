"""
Request entity for ModifyTheParsingRecordStatusRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyTheParsingRecordStatusRequest(AbstractModel):
    """
    Request entity for ModifyTheParsingRecordStatusRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, zone_name, record_id, action, client_token=None):
        """
        Initialize ModifyTheParsingRecordStatusRequest request entity.

        :param zone_name: zone_name parameter
        :type zone_name: str (required)

        :param record_id: record_id parameter
        :type record_id: str (required)

        :param action: action parameter
        :type action: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.record_id = record_id
        self.action = action
        self.client_token = client_token

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
        :rtype: ModifyTheParsingRecordStatusRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
