"""
Table information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.product import Product


class Table(AbstractModel):
    """
    Table
    """

    def __init__(self, product=None, quantity=None, unit_price=None, subtotal_amount=None):
        """
        Initialize Table instance.

        :param product: product attribute
        :type product: Product (optional)

        :param quantity: 数量
        :type quantity: str (optional)

        :param unit_price: 单价
        :type unit_price: str (optional)

        :param subtotal_amount: 小计金额
        :type subtotal_amount: str (optional)
        """
        super().__init__()
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal_amount = subtotal_amount

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
        if self.product is not None:
            result['product'] = self.product.to_dict()
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit_price is not None:
            result['unit_price'] = self.unit_price
        if self.subtotal_amount is not None:
            result['subtotal_amount'] = self.subtotal_amount
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Table

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('product') is not None:
            self.product = Product().from_dict(m.get('product'))
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit_price') is not None:
            self.unit_price = m.get('unit_price')
        if m.get('subtotal_amount') is not None:
            self.subtotal_amount = m.get('subtotal_amount')
        return self
