"""
CatagoryPrice information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CatagoryPrice(AbstractModel):
    """
    CatagoryPrice
    """

    def __init__(self, pre_pay_category_price=None, post_pay_category_price=None):
        """
        Initialize CatagoryPrice instance.

        :param pre_pay_category_price: 实例券预付目录价格。
        :type pre_pay_category_price: float (optional)

        :param post_pay_category_price: 实例券后付价，根据入参 priceTimeUnit 返回按小时计价格或按月计价格。
        :type post_pay_category_price: float (optional)
        """
        super().__init__()
        self.pre_pay_category_price = pre_pay_category_price
        self.post_pay_category_price = post_pay_category_price

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
        if self.pre_pay_category_price is not None:
            result['prePayCategoryPrice'] = self.pre_pay_category_price
        if self.post_pay_category_price is not None:
            result['postPayCategoryPrice'] = self.post_pay_category_price
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CatagoryPrice

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('prePayCategoryPrice') is not None:
            self.pre_pay_category_price = m.get('prePayCategoryPrice')
        if m.get('postPayCategoryPrice') is not None:
            self.post_pay_category_price = m.get('postPayCategoryPrice')
        return self
