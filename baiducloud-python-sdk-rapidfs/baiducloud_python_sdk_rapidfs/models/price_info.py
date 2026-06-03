"""
PriceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PriceInfo(AbstractModel):
    """
    PriceInfo
    """

    def __init__(self, currency=None, unit_price=None, charge_type=None, charge_unit=None):
        """
        Initialize PriceInfo instance.

        :param currency: 货币单位，枚举值：* CNY：人民币，默认；* USD：美元
        :type currency: str (optional)

        :param unit_price: 价格
        :type unit_price: float (optional)

        :param charge_type: 付费类型，当前为 PostPaid，后付费
        :type charge_type: str (optional)

        :param charge_unit: charge_unit attribute
        :type charge_unit: str (optional)
        """
        super().__init__()
        self.currency = currency
        self.unit_price = unit_price
        self.charge_type = charge_type
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
        if self.currency is not None:
            result['currency'] = self.currency
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
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
        :rtype: PriceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargeUnit') is not None:
            self.charge_unit = m.get('chargeUnit')
        return self
