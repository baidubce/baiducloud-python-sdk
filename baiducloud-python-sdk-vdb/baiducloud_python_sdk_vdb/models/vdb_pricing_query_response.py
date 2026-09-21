"""
VdbPricingQueryResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_vdb.models.multi_year_result import MultiYearResult


class VdbPricingQueryResponse(BceResponse):
    """
    VdbPricingQueryResponse
    """

    def __init__(
        self,
        catalog_price=None,
        component_type=None,
        discount=None,
        discount_type=None,
        multi_year_result=None,
        origin_discount=None,
        origin_price=None,
        price=None,
        price_id=None,
        price_name=None,
        price_type=None,
        real_catalog_price=None,
    ):
        """
        Initialize VdbPricingQueryResponse instance.

        :param catalog_price:
        :type catalog_price: float (optional)

        :param component_type:
        :type component_type: str (optional)

        :param discount:
        :type discount: float (optional)

        :param discount_type:
        :type discount_type: str (optional)

        :param multi_year_result: multi_year_result attribute
        :type multi_year_result: MultiYearResult (optional)

        :param origin_discount:
        :type origin_discount: float (optional)

        :param origin_price:
        :type origin_price: float (optional)

        :param price:
        :type price: float (optional)

        :param price_id:
        :type price_id: int (optional)

        :param price_name:
        :type price_name: str (optional)

        :param price_type:
        :type price_type: str (optional)

        :param real_catalog_price:
        :type real_catalog_price: float (optional)
        """
        super().__init__()
        self.catalog_price = catalog_price
        self.component_type = component_type
        self.discount = discount
        self.discount_type = discount_type
        self.multi_year_result = multi_year_result
        self.origin_discount = origin_discount
        self.origin_price = origin_price
        self.price = price
        self.price_id = price_id
        self.price_name = price_name
        self.price_type = price_type
        self.real_catalog_price = real_catalog_price

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.catalog_price is not None:
            result['catalogPrice'] = self.catalog_price
        if self.component_type is not None:
            result['componentType'] = self.component_type
        if self.discount is not None:
            result['discount'] = self.discount
        if self.discount_type is not None:
            result['discountType'] = self.discount_type
        if self.multi_year_result is not None:
            result['multiYearResult'] = self.multi_year_result.to_dict()
        if self.origin_discount is not None:
            result['originDiscount'] = self.origin_discount
        if self.origin_price is not None:
            result['originPrice'] = self.origin_price
        if self.price is not None:
            result['price'] = self.price
        if self.price_id is not None:
            result['priceId'] = self.price_id
        if self.price_name is not None:
            result['priceName'] = self.price_name
        if self.price_type is not None:
            result['priceType'] = self.price_type
        if self.real_catalog_price is not None:
            result['realCatalogPrice'] = self.real_catalog_price
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VdbPricingQueryResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('catalogPrice') is not None:
            self.catalog_price = m.get('catalogPrice')
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('discountType') is not None:
            self.discount_type = m.get('discountType')
        if m.get('multiYearResult') is not None:
            self.multi_year_result = MultiYearResult().from_dict(m.get('multiYearResult'))
        if m.get('originDiscount') is not None:
            self.origin_discount = m.get('originDiscount')
        if m.get('originPrice') is not None:
            self.origin_price = m.get('originPrice')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('priceId') is not None:
            self.price_id = m.get('priceId')
        if m.get('priceName') is not None:
            self.price_name = m.get('priceName')
        if m.get('priceType') is not None:
            self.price_type = m.get('priceType')
        if m.get('realCatalogPrice') is not None:
            self.real_catalog_price = m.get('realCatalogPrice')
        return self
