"""
Request entity for DescribeAppBlbServerGroupRsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAppBlbServerGroupRsRequest(AbstractModel):
    """
    Request entity for DescribeAppBlbServerGroupRsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, sg_id, marker=None, max_keys=None):
        """
        Initialize DescribeAppBlbServerGroupRsRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param sg_id: sg_id parameter
        :type sg_id: str (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.sg_id = sg_id
        self.marker = marker
        self.max_keys = max_keys

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
        :rtype: DescribeAppBlbServerGroupRsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('sgId') is not None:
            self.sg_id = m.get('sgId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
