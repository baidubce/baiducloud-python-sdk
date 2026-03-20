"""
Request entity for CreateVpcResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateVpcResponse(BceResponse):
    """
    CreateVpcResponse
    """

    def __init__(self, vpc_id=None):
        """
        Initialize CreateVpcResponse response.

        :param vpc_id: 创建VPC的id
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVpcResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
