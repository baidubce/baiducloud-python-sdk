"""
Request entity for ResizeTbspRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeTbspRequest(AbstractModel):
    """
    Request entity for ResizeTbspRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, ip_capacity, client_token=None):
        """
        Initialize ResizeTbspRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_capacity: DDoS增强防护包IP容量，需大于升级前的IP容量（5/30/100）
        :type ip_capacity: int (required)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip_capacity = ip_capacity

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
        if self.ip_capacity is not None:
            result['ipCapacity'] = self.ip_capacity
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeTbspRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipCapacity') is not None:
            self.ip_capacity = m.get('ipCapacity')
        return self
