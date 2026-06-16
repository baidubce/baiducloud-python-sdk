"""
Request entity for GetBidInstancePriceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetBidInstancePriceResponse(BceResponse):
    """
    GetBidInstancePriceResponse
    """

    def __init__(self, money=None, count=None, original_money=None, per_original_money=None, per_money=None):
        """
        Initialize GetBidInstancePriceResponse response.

        :param money: 总价
        :type money: str (optional)

        :param count: 购买个数
        :type count: str (optional)

        :param original_money: 原价总价
        :type original_money: str (optional)

        :param per_original_money: 原价单价
        :type per_original_money: str (optional)

        :param per_money: 单个价格
        :type per_money: str (optional)
        """
        super().__init__()
        self.money = money
        self.count = count
        self.original_money = original_money
        self.per_original_money = per_original_money
        self.per_money = per_money

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
        if self.money is not None:
            result['money'] = self.money
        if self.count is not None:
            result['count'] = self.count
        if self.original_money is not None:
            result['originalMoney'] = self.original_money
        if self.per_original_money is not None:
            result['perOriginalMoney'] = self.per_original_money
        if self.per_money is not None:
            result['perMoney'] = self.per_money
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetBidInstancePriceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('money') is not None:
            self.money = m.get('money')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('originalMoney') is not None:
            self.original_money = m.get('originalMoney')
        if m.get('perOriginalMoney') is not None:
            self.per_original_money = m.get('perOriginalMoney')
        if m.get('perMoney') is not None:
            self.per_money = m.get('perMoney')
        return self
