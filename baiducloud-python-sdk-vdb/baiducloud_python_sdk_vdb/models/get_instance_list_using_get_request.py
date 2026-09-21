"""
Request entity for GetInstanceListUsingGetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetInstanceListUsingGetRequest(AbstractModel):
    """
    Request entity for GetInstanceListUsingGetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, engine_type=None, instance_type=None):
        """
        Initialize GetInstanceListUsingGetRequest request entity.

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param instance_type: instance_type parameter
        :type instance_type: str (optional)
        """
        super().__init__()
        self.engine_type = engine_type
        self.instance_type = instance_type

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
        :rtype: GetInstanceListUsingGetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self
