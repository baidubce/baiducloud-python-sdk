"""
Request entity for DescribeIndexRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeIndexRequest(AbstractModel):
    """
    Request entity for DescribeIndexRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_store_name, project=None):
        """
        Initialize DescribeIndexRequest request entity.

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (required)

        :param project: project parameter
        :type project: str (optional)
        """
        super().__init__()
        self.log_store_name = log_store_name
        self.project = project

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
        :rtype: DescribeIndexRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self
