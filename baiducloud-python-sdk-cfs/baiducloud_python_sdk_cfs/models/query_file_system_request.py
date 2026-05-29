"""
Request entity for QueryFileSystemRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryFileSystemRequest(AbstractModel):
    """
    Request entity for QueryFileSystemRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_id, fs_id=None, marker=None, max_keys=None, filter_tag=None):
        """
        Initialize QueryFileSystemRequest request entity.

        :param user_id: user_id parameter
        :type user_id: str (required)

        :param fs_id: fs_id parameter
        :type fs_id: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param filter_tag: filter_tag parameter
        :type filter_tag: str (optional)
        """
        super().__init__()
        self.user_id = user_id
        self.fs_id = fs_id
        self.marker = marker
        self.max_keys = max_keys
        self.filter_tag = filter_tag

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
        :rtype: QueryFileSystemRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('filterTag') is not None:
            self.filter_tag = m.get('filterTag')
        return self
