"""
RobotPermissionAccess information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RobotPermissionAccess(AbstractModel):
    """
    RobotPermissionAccess
    """

    def __init__(self, resource=None, action=None):
        """
        Initialize RobotPermissionAccess instance.

        :param resource: 固定值为 `repository`
        :type resource: str (optional)

        :param action: 访问权限内容，`pull` 对应镜像拉取权限，`push` 对应镜像推送权限
        :type action: str (optional)
        """
        super().__init__()
        self.resource = resource
        self.action = action

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
        if self.resource is not None:
            result['resource'] = self.resource
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RobotPermissionAccess

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self
