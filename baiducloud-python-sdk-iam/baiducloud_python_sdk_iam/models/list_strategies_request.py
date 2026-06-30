"""
Request entity for ListStrategiesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListStrategiesRequest(AbstractModel):
    """
    Request entity for ListStrategiesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, policy_type=None, name_filter=None):
        """
        Initialize ListStrategiesRequest request entity.

        :param policy_type: policy_type parameter
        :type policy_type: str (optional)

        :param name_filter: name_filter parameter
        :type name_filter: str (optional)
        """
        super().__init__()
        self.policy_type = policy_type
        self.name_filter = name_filter

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
        :rtype: ListStrategiesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('nameFilter') is not None:
            self.name_filter = m.get('nameFilter')
        return self
