"""
RobotPermission information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.robot_permission_access import RobotPermissionAccess


class RobotPermission(AbstractModel):
    """
    RobotPermission
    """

    def __init__(self, kind=None, namespace=None, access=None):
        """
        Initialize RobotPermission instance.

        :param kind: 固定值为 `project`
        :type kind: str (optional)

        :param namespace: 命名空间名称，如果是选择所有命名空间，则展示 `*`
        :type namespace: str (optional)

        :param access: 访问权限内容
        :type access: List[RobotPermissionAccess] (optional)
        """
        super().__init__()
        self.kind = kind
        self.namespace = namespace
        self.access = access

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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.access is not None:
            result['access'] = [i.to_dict() for i in self.access]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RobotPermission

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('access') is not None:
            self.access = [RobotPermissionAccess().from_dict(i) for i in m.get('access')]
        return self
