"""
Request entity for DescribeTokenRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeTokenRequest(AbstractModel):
    """
    Request entity for DescribeTokenRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, token_id=None):
        """
        Initialize DescribeTokenRequest request entity.

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param token_id: Token id，不传返回集群默认 Token
        :type token_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.token_id = token_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeTokenRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        return self
