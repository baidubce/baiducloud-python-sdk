"""
Request entity for GetPriceUsingPOSTResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vdb.models.vdb_pricing_query_response import VdbPricingQueryResponse


class GetPriceUsingPOSTResponse(BceResponse):
    """
    GetPriceUsingPOSTResponse
    """

    def __init__(
        self,
        catalog_price=None,
        discount=None,
        discount_type=None,
        price=None,
        price_details=None,
        real_catalog_price=None,
    ):
        """
        Initialize GetPriceUsingPOSTResponse response.

        :param catalog_price: catalog_price field
        :type catalog_price: float (optional)

        :param discount: discount field
        :type discount: float (optional)

        :param discount_type: discount_type field
        :type discount_type: str (optional)

        :param price: price field
        :type price: float (optional)

        :param price_details: price_details field
        :type price_details: List[VdbPricingQueryResponse] (optional)

        :param real_catalog_price: real_catalog_price field
        :type real_catalog_price: float (optional)
        """
        super().__init__()
        self.catalog_price = catalog_price
        self.discount = discount
        self.discount_type = discount_type
        self.price = price
        self.price_details = price_details
        self.real_catalog_price = real_catalog_price

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
        if self.catalog_price is not None:
            result['catalogPrice'] = self.catalog_price
        if self.discount is not None:
            result['discount'] = self.discount
        if self.discount_type is not None:
            result['discountType'] = self.discount_type
        if self.price is not None:
            result['price'] = self.price
        if self.price_details is not None:
            result['priceDetails'] = [i.to_dict() for i in self.price_details]
        if self.real_catalog_price is not None:
            result['realCatalogPrice'] = self.real_catalog_price
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPriceUsingPOSTResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('catalogPrice') is not None:
            self.catalog_price = m.get('catalogPrice')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('discountType') is not None:
            self.discount_type = m.get('discountType')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('priceDetails') is not None:
            self.price_details = [VdbPricingQueryResponse().from_dict(i) for i in m.get('priceDetails')]
        if m.get('realCatalogPrice') is not None:
            self.real_catalog_price = m.get('realCatalogPrice')
        return self
