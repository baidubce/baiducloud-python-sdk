"""
Request entity for DeleteFastQueryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteFastQueryRequest(AbstractModel):
    """
    Request entity for DeleteFastQueryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, fast_query_name):
        """
        Initialize DeleteFastQueryRequest request entity.

        :param fast_query_name: fast_query_name parameter
        :type fast_query_name: str (required)
        """
        super().__init__()
        self.fast_query_name = fast_query_name

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
        :rtype: DeleteFastQueryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fastQueryName') is not None:
            self.fast_query_name = m.get('fastQueryName')
        return self
