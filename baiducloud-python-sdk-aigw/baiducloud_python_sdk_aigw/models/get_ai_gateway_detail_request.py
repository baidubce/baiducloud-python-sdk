"""
Request entity for GetAiGatewayDetailRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetAiGatewayDetailRequest(AbstractModel):
    """
    Request entity for GetAiGatewayDetailRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, x_region, src_product=None):
        """
        Initialize GetAiGatewayDetailRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param src_product: src_product parameter
        :type src_product: str (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.src_product = src_product
        self.x_region = x_region

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
        :rtype: GetAiGatewayDetailRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
