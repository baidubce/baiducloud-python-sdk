"""
Request entity for DeleteLogStoreViewRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteLogStoreViewRequest(AbstractModel):
    """
    Request entity for DeleteLogStoreViewRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, project=None):
        """
        Initialize DeleteLogStoreViewRequest request entity.

        :param name: 日志视图名称
        :type name: str (required)

        :param project: 日志组名称
        :type project: str (optional)
        """
        super().__init__()
        self.name = name
        self.project = project

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
        if self.name is not None:
            result['name'] = self.name
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteLogStoreViewRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self
