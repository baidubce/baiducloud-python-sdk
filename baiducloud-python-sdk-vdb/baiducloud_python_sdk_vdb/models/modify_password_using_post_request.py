"""
Request entity for ModifyPasswordUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyPasswordUsingPOSTRequest(AbstractModel):
    """
    Request entity for ModifyPasswordUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, engine_type=None, vdb_from=None, password=None, username=None):
        """
        Initialize ModifyPasswordUsingPOSTRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param vdb_from: vdb_from parameter
        :type vdb_from: str (optional)

        :param password: password parameter
        :type password: str (optional)

        :param username: username parameter
        :type username: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.engine_type = engine_type
        self.vdb_from = vdb_from
        self.password = password
        self.username = username

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
        if self.vdb_from is not None:
            result['from'] = self.vdb_from
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyPasswordUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('from') is not None:
            self.vdb_from = m.get('from')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self
