"""
Request entity for CreateSubnetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateSubnetResponse(BceResponse):
    """
    CreateSubnetResponse
    """

    def __init__(self, subnet_id=None):
        """
        Initialize CreateSubnetResponse response.

        :param subnet_id: 创建子网的ID
        :type subnet_id: str (optional)
        """
        super().__init__()
        self.subnet_id = subnet_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSubnetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self
