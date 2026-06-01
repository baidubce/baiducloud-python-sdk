"""
Request entity for QueryDedicatedChannelRouteRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryDedicatedChannelRouteRulesRequest(AbstractModel):
    """
    Request entity for QueryDedicatedChannelRouteRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_id, et_channel_id, marker=None, max_keys=None, dest_address=None):
        """
        Initialize QueryDedicatedChannelRouteRulesRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param dest_address: dest_address parameter
        :type dest_address: str (optional)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.marker = marker
        self.max_keys = max_keys
        self.dest_address = dest_address

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
        :rtype: QueryDedicatedChannelRouteRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('etChannelId') is not None:
            self.et_channel_id = m.get('etChannelId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('destAddress') is not None:
            self.dest_address = m.get('destAddress')
        return self
