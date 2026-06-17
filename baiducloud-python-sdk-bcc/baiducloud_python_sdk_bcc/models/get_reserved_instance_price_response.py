"""
Request entity for GetReservedInstancePriceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetReservedInstancePriceResponse(BceResponse):
    """
    GetReservedInstancePriceResponse
    """

    def __init__(self, request_id=None, spec=None, category_price=None, trade_price=None):
        """
        Initialize GetReservedInstancePriceResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param spec: 实例券规格。
        :type spec: str (optional)

        :param category_price: 实例券目录价格。
        :type category_price: object (optional)

        :param trade_price: 实例券最终价，即优惠后订单实付价格。
        :type trade_price: object (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.spec = spec
        self.category_price = category_price
        self.trade_price = trade_price

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.spec is not None:
            result['spec'] = self.spec
        if self.category_price is not None:
            result['categoryPrice'] = self.category_price
        if self.trade_price is not None:
            result['tradePrice'] = self.trade_price
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetReservedInstancePriceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('categoryPrice') is not None:
            self.category_price = m.get('categoryPrice')
        if m.get('tradePrice') is not None:
            self.trade_price = m.get('tradePrice')
        return self
