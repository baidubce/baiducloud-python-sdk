"""
Request entity for ModifyParametersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.parameter import Parameter


class ModifyParametersRequest(AbstractModel):
    """
    Request entity for ModifyParametersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, parameter):
        """
        Initialize ModifyParametersRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param parameter: parameter parameter
        :type parameter: Parameter (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.parameter = parameter

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
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyParametersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('parameter') is not None:
            self.parameter = Parameter().from_dict(m.get('parameter'))
        return self
