"""
TradePrice information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TradePrice(AbstractModel):
    """
    TradePrice
    """

    def __init__(self, pre_pay_trade_price=None, post_pay_trade_price=None):
        """
        Initialize TradePrice instance.

        :param pre_pay_trade_price: 实例券折后预付价。
        :type pre_pay_trade_price: float (optional)

        :param post_pay_trade_price: 实例券折后后付价。
        :type post_pay_trade_price: float (optional)
        """
        super().__init__()
        self.pre_pay_trade_price = pre_pay_trade_price
        self.post_pay_trade_price = post_pay_trade_price

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.pre_pay_trade_price is not None:
            result['prePayTradePrice'] = self.pre_pay_trade_price
        if self.post_pay_trade_price is not None:
            result['postPayTradePrice'] = self.post_pay_trade_price
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TradePrice

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('prePayTradePrice') is not None:
            self.pre_pay_trade_price = m.get('prePayTradePrice')
        if m.get('postPayTradePrice') is not None:
            self.post_pay_trade_price = m.get('postPayTradePrice')
        return self
