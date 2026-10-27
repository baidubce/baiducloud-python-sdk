"""
Request entity for ListL3ClientsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListL3ClientsRequest(AbstractModel):
    """
    Request entity for ListL3ClientsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, marker=None, max_keys=None):
        """
        Initialize ListL3ClientsRequest request entity.

        :param instance_id: PFS 实例 ID
        :type instance_id: str (required)

        :param marker: 按 clientIp 的字典序排列，从 marker 之后开始返回（不含 marker），默认空串
        :type marker: str (optional)

        :param max_keys: 本次最多返回的客户端数量，默认 1000；传 ≤ 0 会被纠正为 1，传 > 1000 会被纠正为 1000
        :type max_keys: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL3ClientsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
