"""
Request entity for ListInstanceByIdsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListInstanceByIdsRequest(AbstractModel):
    """
    Request entity for ListInstanceByIdsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_ids, marker=None, max_keys=None):
        """
        Initialize ListInstanceByIdsRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param instance_ids: 待查询的实例id列表，最多支持100个
        :type instance_ids: List[str] (required)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.instance_ids = instance_ids

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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListInstanceByIdsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        return self
