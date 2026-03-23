"""
Price information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Price(AbstractModel):
    """
    Price
    """

    def __init__(self, charge_item=None, discount_price=None, original_price=None, charge_unit=None):
        """
        Initialize Price instance.

        :param charge_item: 计费项，比如取值\"instance\"代表实例费用；比如\"netraffic\"代表流量费用
        :type charge_item: str (optional)

        :param discount_price: 折扣价，单位都是元。预付费的时候，返回值比如：\"150\"，后付费的时候，返回值比如：\"0.00028\"
        :type discount_price: str (optional)

        :param original_price: 原价
        :type original_price: str (optional)

        :param charge_unit: 计费单位。后付费的时候取值，比如\"minute\"。minute：表示计价单元是按每分钟来计算。GB：表示计价单元是按每GB来计算。 \"lcu\"代表按每lcu单位计费
        :type charge_unit: str (optional)
        """
        super().__init__()
        self.charge_item = charge_item
        self.discount_price = discount_price
        self.original_price = original_price
        self.charge_unit = charge_unit

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
        if self.charge_item is not None:
            result['chargeItem'] = self.charge_item
        if self.discount_price is not None:
            result['discountPrice'] = self.discount_price
        if self.original_price is not None:
            result['originalPrice'] = self.original_price
        if self.charge_unit is not None:
            result['chargeUnit'] = self.charge_unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Price

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('chargeItem') is not None:
            self.charge_item = m.get('chargeItem')
        if m.get('discountPrice') is not None:
            self.discount_price = m.get('discountPrice')
        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')
        if m.get('chargeUnit') is not None:
            self.charge_unit = m.get('chargeUnit')
        return self
