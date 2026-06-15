"""
Request entity for BindRoleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.instance_pass_role_model import InstancePassRoleModel


class BindRoleRequest(AbstractModel):
    """
    Request entity for BindRoleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instances, role_name=None):
        """
        Initialize BindRoleRequest request entity.

        :param role_name: 实例绑定的角色名称
        :type role_name: str (optional)

        :param instances: 要绑定角色的实例id列表
        :type instances: List[InstancePassRoleModel] (required)
        """
        super().__init__()
        self.role_name = role_name
        self.instances = instances

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
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindRoleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('instances') is not None:
            self.instances = [InstancePassRoleModel().from_dict(i) for i in m.get('instances')]
        return self
