"""
Request entity for BindingTagsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.resource import Resource


class BindingTagsRequest(AbstractModel):
    """
    Request entity for BindingTagsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, resources):
        """
        Initialize BindingTagsRequest request entity.

        :param resources: 资源列表
        :type resources: List[Resource] (required)
        """
        super().__init__()
        self.resources = resources

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
        if self.resources is not None:
            result['resources'] = [i.to_dict() for i in self.resources]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindingTagsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resources') is not None:
            self.resources = [Resource().from_dict(i) for i in m.get('resources')]
        return self
