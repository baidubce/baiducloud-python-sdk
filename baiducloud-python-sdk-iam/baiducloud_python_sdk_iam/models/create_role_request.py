"""
Request entity for CreateRoleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateRoleRequest(AbstractModel):
    """
    Request entity for CreateRoleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, assume_role_policy_document, description=None, grant_type=None):
        """
        Initialize CreateRoleRequest request entity.

        :param name: 角色名
        :type name: str (required)

        :param description: 角色的描述
        :type description: str (optional)

        :param grant_type: 扮演角色的载体类型
        :type grant_type: str (optional)

        :param assume_role_policy_document: 指定允许扮演角色的载体
        :type assume_role_policy_document: str (required)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.grant_type = grant_type
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
        if self.grant_type is not None:
            result['grantType'] = self.grant_type
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
        :rtype: CreateRoleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('grantType') is not None:
            self.grant_type = m.get('grantType')
        if m.get('assumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('assumeRolePolicyDocument')
        return self
