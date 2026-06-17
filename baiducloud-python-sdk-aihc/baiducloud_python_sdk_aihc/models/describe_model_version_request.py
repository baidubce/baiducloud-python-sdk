"""
Request entity for DescribeModelVersionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeModelVersionRequest(AbstractModel):
    """
    Request entity for DescribeModelVersionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, model_id, version_id):
        """
        Initialize DescribeModelVersionRequest request entity.

        :param model_id: model_id parameter
        :type model_id: str (required)

        :param version_id: version_id parameter
        :type version_id: str (required)
        """
        super().__init__()
        self.model_id = model_id
        self.version_id = version_id

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
        :rtype: DescribeModelVersionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self
