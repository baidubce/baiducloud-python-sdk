"""
Request entity for DescribeAppBlbRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAppBlbRequest(AbstractModel):
    """
    Request entity for DescribeAppBlbRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id):
        """
        Initialize DescribeAppBlbRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)
        """
        super().__init__()
        self.blb_id = blb_id

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
        :rtype: DescribeAppBlbRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        return self
