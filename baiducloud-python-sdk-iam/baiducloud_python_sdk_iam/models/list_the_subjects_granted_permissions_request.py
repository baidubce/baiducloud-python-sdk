"""
Request entity for ListTheSubjectsGrantedPermissionsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListTheSubjectsGrantedPermissionsRequest(AbstractModel):
    """
    Request entity for ListTheSubjectsGrantedPermissionsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, policy_id, grant_type):
        """
        Initialize ListTheSubjectsGrantedPermissionsRequest request entity.

        :param policy_id: policy_id parameter
        :type policy_id: str (required)

        :param grant_type: grant_type parameter
        :type grant_type: str (required)
        """
        super().__init__()
        self.policy_id = policy_id
        self.grant_type = grant_type

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
        :rtype: ListTheSubjectsGrantedPermissionsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('grantType') is not None:
            self.grant_type = m.get('grantType')
        return self
