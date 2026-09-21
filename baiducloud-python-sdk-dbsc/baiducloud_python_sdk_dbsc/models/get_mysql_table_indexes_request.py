"""
Request entity for GetMysqlTableIndexesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetMysqlTableIndexesRequest(AbstractModel):
    """
    Request entity for GetMysqlTableIndexesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id):
        """
        Initialize GetMysqlTableIndexesRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)
        """
        super().__init__()
        self.app_id = app_id

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
        :rtype: GetMysqlTableIndexesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self
