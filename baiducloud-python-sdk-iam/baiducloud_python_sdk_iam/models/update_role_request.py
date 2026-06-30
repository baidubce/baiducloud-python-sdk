"""
Request entity for UpdateRoleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateRoleRequest(AbstractModel):
    """
    Request entity for UpdateRoleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, role_name, name=None, description=None, assume_role_policy_document=None):
        """
        Initialize UpdateRoleRequest request entity.

        :param role_name: role_name parameter
        :type role_name: str (required)

        :param name: 更新后的角色名
        :type name: str (optional)

        :param description: 角色的描述
        :type description: str (optional)

        :param assume_role_policy_document: 指定可以扮演此角色的身份
        :type assume_role_policy_document: str (optional)
        """
        super().__init__()
        self.role_name = role_name
        self.name = name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document

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
        if self.description is not None:
            result['description'] = self.description
        if self.assume_role_policy_document is not None:
            result['assumeRolePolicyDocument'] = self.assume_role_policy_document
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateRoleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('assumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('assumeRolePolicyDocument')
        return self
