"""
Request entity for QueryMountingTargetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryMountingTargetRequest(AbstractModel):
    """
    Request entity for QueryMountingTargetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, f_id, mount_id=None, marker=None, max_keys=None):
        """
        Initialize QueryMountingTargetRequest request entity.

        :param f_id: f_id parameter
        :type f_id: str (required)

        :param mount_id: mount_id parameter
        :type mount_id: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.f_id = f_id
        self.mount_id = mount_id
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
        :rtype: QueryMountingTargetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fId') is not None:
            self.f_id = m.get('fId')
        if m.get('mountId') is not None:
            self.mount_id = m.get('mountId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
