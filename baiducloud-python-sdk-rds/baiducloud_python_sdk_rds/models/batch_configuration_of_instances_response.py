"""
Request entity for BatchConfigurationOfInstancesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class BatchConfigurationOfInstancesResponse(BceResponse):
    """
    BatchConfigurationOfInstancesResponse
    """

    def __init__(self, order_list=None):
        """
        Initialize BatchConfigurationOfInstancesResponse response.

        :param order_list: 批量变配的订单号数组
        :type order_list: List[str] (optional)
        """
        super().__init__()
        self.order_list = order_list

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
        if self.order_list is not None:
            result['orderList'] = self.order_list
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchConfigurationOfInstancesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderList') is not None:
            self.order_list = m.get('orderList')
        return self
