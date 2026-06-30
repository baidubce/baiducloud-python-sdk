"""
Request entity for AssociateGroupPermissionsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AssociateGroupPermissionsRequest(AbstractModel):
    """
    Request entity for AssociateGroupPermissionsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_name, policy_name, policy_type=None):
        """
        Initialize AssociateGroupPermissionsRequest request entity.

        :param group_name: group_name parameter
        :type group_name: str (required)

        :param policy_name: policy_name parameter
        :type policy_name: str (required)

        :param policy_type: policy_type parameter
        :type policy_type: str (optional)
        """
        super().__init__()
        self.group_name = group_name
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
        :rtype: AssociateGroupPermissionsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self
