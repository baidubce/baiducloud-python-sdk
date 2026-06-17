"""
Request entity for DescribeLogStoreTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeLogStoreTemplateRequest(AbstractModel):
    """
    Request entity for DescribeLogStoreTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name):
        """
        Initialize DescribeLogStoreTemplateRequest request entity.

        :param name: 模板名称
        :type name: str (required)
        """
        super().__init__()
        self.name = name

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
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLogStoreTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
