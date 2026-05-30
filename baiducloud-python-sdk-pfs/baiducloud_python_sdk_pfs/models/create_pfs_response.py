"""
Request entity for CreatePfsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreatePfsResponse(BceResponse):
    """
    CreatePfsResponse
    """

    def __init__(self, instance_id=None, order_id=None):
        """
        Initialize CreatePfsResponse response.

        :param instance_id: 实例Id
        :type instance_id: str (optional)

        :param order_id: 订单id
        :type order_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.order_id = order_id

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
            result['metadata'] = dict(self.metadata)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePfsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self
