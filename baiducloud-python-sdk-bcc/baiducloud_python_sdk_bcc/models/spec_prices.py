"""
SpecPrices information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SpecPrices(AbstractModel):
    """
    SpecPrices
    """

    def __init__(self, spec=None, spec_price=None, discount=None, trade_price=None, status=None):
        """
        Initialize SpecPrices instance.

        :param spec: 实例规格
        :type spec: str (optional)

        :param spec_price: 目录价
        :type spec_price: str (optional)

        :param discount: 折扣
        :type discount: str (optional)

        :param trade_price: 优惠后价格
        :type trade_price: str (optional)

        :param status: 状态
        :type status: str (optional)
        """
        super().__init__()
        self.spec = spec
        self.spec_price = spec_price
        self.discount = discount
        self.trade_price = trade_price
        self.status = status

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
        if self.spec is not None:
            result['spec'] = self.spec
        if self.spec_price is not None:
            result['specPrice'] = self.spec_price
        if self.discount is not None:
            result['discount'] = self.discount
        if self.trade_price is not None:
            result['tradePrice'] = self.trade_price
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SpecPrices

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('specPrice') is not None:
            self.spec_price = m.get('specPrice')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('tradePrice') is not None:
            self.trade_price = m.get('tradePrice')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
