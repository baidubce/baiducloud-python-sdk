"""
Request entity for DescribeOrderResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.order_info import OrderInfo


class DescribeOrderResponse(BceResponse):
    """
    DescribeOrderResponse
    """

    def __init__(self, order_info=None):
        """
        Initialize DescribeOrderResponse response.

        :param order_info: order_info field
        :type order_info: OrderInfo (optional)
        """
        super().__init__()
        self.order_info = order_info

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
        if self.order_info is not None:
            result['orderInfo'] = self.order_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeOrderResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderInfo') is not None:
            self.order_info = OrderInfo().from_dict(m.get('orderInfo'))
        return self
