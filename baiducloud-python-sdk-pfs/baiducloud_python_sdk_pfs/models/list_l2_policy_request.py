"""
Request entity for ListL2PolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListL2PolicyRequest(AbstractModel):
    """
    Request entity for ListL2PolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, max_keys=None, marker=None):
        """
        Initialize ListL2PolicyRequest request entity.

        :param instance_id: policyId对应的pfs实例短id
        :type instance_id: str (required)

        :param max_keys: 本次请求返回数量，默认为20
        :type max_keys: int (optional)

        :param marker: 上一次返回的nextMarker的值，用于分段遍历list所有task使用，下次将从该makrer处继续往后返回值
        :type marker: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.max_keys = max_keys
        self.marker = marker

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
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL2PolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
