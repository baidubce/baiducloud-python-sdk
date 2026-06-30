"""
Request entity for DeleteStrategyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteStrategyRequest(AbstractModel):
    """
    Request entity for DeleteStrategyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, policy_name):
        """
        Initialize DeleteStrategyRequest request entity.

        :param policy_name: policy_name parameter
        :type policy_name: str (required)
        """
        super().__init__()
        self.policy_name = policy_name

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
        :rtype: DeleteStrategyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        return self
