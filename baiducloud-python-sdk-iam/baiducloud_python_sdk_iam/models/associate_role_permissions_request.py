"""
Request entity for AssociateRolePermissionsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AssociateRolePermissionsRequest(AbstractModel):
    """
    Request entity for AssociateRolePermissionsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, role_name, policy_name, policy_type=None):
        """
        Initialize AssociateRolePermissionsRequest request entity.

        :param role_name: role_name parameter
        :type role_name: str (required)

        :param policy_name: policy_name parameter
        :type policy_name: str (required)

        :param policy_type: policy_type parameter
        :type policy_type: str (optional)
        """
        super().__init__()
        self.role_name = role_name
        self.policy_name = policy_name
        self.policy_type = policy_type

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
        :rtype: AssociateRolePermissionsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self
