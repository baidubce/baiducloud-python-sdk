"""
Request entity for DescribeSpecsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rapidfs.models.filter import Filter


class DescribeSpecsRequest(AbstractModel):
    """
    Request entity for DescribeSpecsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, filters=None):
        """
        Initialize DescribeSpecsRequest request entity.

        :param filters: filters parameter
        :type filters: List[Filter] (optional)
        """
        super().__init__()
        self.filters = filters

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
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeSpecsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        return self
