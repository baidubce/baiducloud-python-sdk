"""
Request entity for UpdateInstanceNameUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateInstanceNameUsingPOSTRequest(AbstractModel):
    """
    Request entity for UpdateInstanceNameUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, engine_type=None, instance_name=None):
        """
        Initialize UpdateInstanceNameUsingPOSTRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param instance_name: instance_name parameter
        :type instance_name: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.engine_type = engine_type
        self.instance_name = instance_name

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
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateInstanceNameUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        return self
