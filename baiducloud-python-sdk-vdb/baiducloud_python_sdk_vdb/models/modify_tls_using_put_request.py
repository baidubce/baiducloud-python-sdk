"""
Request entity for ModifyTLSUsingPUTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyTLSUsingPUTRequest(AbstractModel):
    """
    Request entity for ModifyTLSUsingPUTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, engine_type=None, action=None, instance_id=None):
        """
        Initialize ModifyTLSUsingPUTRequest request entity.

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param action: action parameter
        :type action: str (optional)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)
        """
        super().__init__()
        self.engine_type = engine_type
        self.action = action
        self.instance_id = instance_id

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
        if self.action is not None:
            result['action'] = self.action
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyTLSUsingPUTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
