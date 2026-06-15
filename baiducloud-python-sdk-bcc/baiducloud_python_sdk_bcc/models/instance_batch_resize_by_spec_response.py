"""
Request entity for InstanceBatchResizeBySpecResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class InstanceBatchResizeBySpecResponse(BceResponse):
    """
    InstanceBatchResizeBySpecResponse
    """

    def __init__(self, order_uuid_results=None):
        """
        Initialize InstanceBatchResizeBySpecResponse response.

        :param order_uuid_results: 变配订单ID列表
        :type order_uuid_results: List[str] (optional)
        """
        super().__init__()
        self.order_uuid_results = order_uuid_results

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
        if self.order_uuid_results is not None:
            result['orderUuidResults'] = self.order_uuid_results
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceBatchResizeBySpecResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderUuidResults') is not None:
            self.order_uuid_results = m.get('orderUuidResults')
        return self
