"""
DeleteRouteResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteRouteResult(AbstractModel):
    """
    DeleteRouteResult
    """

    def __init__(self, route_name=None, deleted_time=None):
        """
        Initialize DeleteRouteResult instance.

        :param route_name: 已删除的路由名称
        :type route_name: str (optional)

        :param deleted_time: 删除时间，格式为 `YYYY-MM-DD HH:mm:ss`
        :type deleted_time: str (optional)
        """
        super().__init__()
        self.route_name = route_name
        self.deleted_time = deleted_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.route_name is not None:
            result['routeName'] = self.route_name
        if self.deleted_time is not None:
            result['deletedTime'] = self.deleted_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteRouteResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        if m.get('deletedTime') is not None:
            self.deleted_time = m.get('deletedTime')
        return self
