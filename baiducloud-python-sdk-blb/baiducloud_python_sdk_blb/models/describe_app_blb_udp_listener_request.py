"""
Request entity for DescribeAppBlbUdpListenerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAppBlbUdpListenerRequest(AbstractModel):
    """
    Request entity for DescribeAppBlbUdpListenerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, listener_port=None, marker=None, max_keys=None):
        """
        Initialize DescribeAppBlbUdpListenerRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param listener_port: listener_port parameter
        :type listener_port: int (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.listener_port = listener_port
        self.marker = marker
        self.max_keys = max_keys

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
        :rtype: DescribeAppBlbUdpListenerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
