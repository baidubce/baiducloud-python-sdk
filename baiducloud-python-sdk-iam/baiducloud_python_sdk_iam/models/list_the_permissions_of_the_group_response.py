"""
Request entity for ListThePermissionsOfTheGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.policy_model import PolicyModel


class ListThePermissionsOfTheGroupResponse(BceResponse):
    """
    ListThePermissionsOfTheGroupResponse
    """

    def __init__(self, policies=None):
        """
        Initialize ListThePermissionsOfTheGroupResponse response.

        :param policies: 策略对象的列表
        :type policies: List[PolicyModel] (optional)
        """
        super().__init__()
        self.policies = policies

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.policies is not None:
            result['policies'] = [i.to_dict() for i in self.policies]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListThePermissionsOfTheGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policies') is not None:
            self.policies = [PolicyModel().from_dict(i) for i in m.get('policies')]
        return self
