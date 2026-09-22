"""
Request entity for PasswordUsingGetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PasswordUsingGetRequest(AbstractModel):
    """
    Request entity for PasswordUsingGetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id=None, username=None, engine_type=None):
        """
        Initialize PasswordUsingGetRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param username: username parameter
        :type username: str (optional)

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.username = username
        self.engine_type = engine_type

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
        :rtype: PasswordUsingGetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        return self
