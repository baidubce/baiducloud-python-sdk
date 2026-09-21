"""
Request entity for GetPriceUsingPostRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetPriceUsingPostRequest(AbstractModel):
    """
    Request entity for GetPriceUsingPostRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, engine_type=None):
        """
        Initialize GetPriceUsingPostRequest request entity.

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)
        """
        super().__init__()
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
        :rtype: GetPriceUsingPostRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        return self
