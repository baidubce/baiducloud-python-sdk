"""
Request entity for GetClusterBlbStatusResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetClusterBlbStatusResponse(BceResponse):
    """
    GetClusterBlbStatusResponse
    """

    def __init__(self, alive=None, errors=None):
        """
        Initialize GetClusterBlbStatusResponse response.

        :param alive: 实例blb状态。
        :type alive: bool (optional)

        :param errors: 报错信息。
        :type errors: str (optional)
        """
        super().__init__()
        self.alive = alive
        self.errors = errors

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.alive is not None:
            result['alive'] = self.alive
        if self.errors is not None:
            result['errors'] = self.errors
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetClusterBlbStatusResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('alive') is not None:
            self.alive = m.get('alive')
        if m.get('errors') is not None:
            self.errors = m.get('errors')
        return self
