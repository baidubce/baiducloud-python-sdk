"""
Request entity for CloseVpcRelayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CloseVpcRelayRequest(AbstractModel):
    """
    Request entity for CloseVpcRelayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, client_token=None):
        """
        Initialize CloseVpcRelayRequest request entity.

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.client_token = client_token

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
        :rtype: CloseVpcRelayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
