"""
Request entity for GenerateInstanceTokenRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GenerateInstanceTokenRequest(AbstractModel):
    """
    Request entity for GenerateInstanceTokenRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, action=None, token=None):
        """
        Initialize GenerateInstanceTokenRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: action parameter
        :type action: str (optional)

        :param token: token parameter
        :type token: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action
        self.token = token

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
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GenerateInstanceTokenRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self
