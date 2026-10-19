"""
Request entity for ObtainThePriceDifferenceOfPrepaidTransformerResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ObtainThePriceDifferenceOfPrepaidTransformerResponse(BceResponse):
    """
    ObtainThePriceDifferenceOfPrepaidTransformerResponse
    """

    def __init__(
        self,
        price=None,
        catalog_price=None,
        traffic_in_gb=None,
        discount=None,
        real_catalog_price=None,
        backup_in_gb=None,
        discount_rate=None,
    ):
        """
        Initialize ObtainThePriceDifferenceOfPrepaidTransformerResponse response.

        :param price: price field
        :type price: object (optional)

        :param catalog_price: catalog_price field
        :type catalog_price: object (optional)

        :param traffic_in_gb: traffic_in_gb field
        :type traffic_in_gb: object (optional)

        :param discount: discount field
        :type discount: object (optional)

        :param real_catalog_price: real_catalog_price field
        :type real_catalog_price: object (optional)

        :param backup_in_gb: backup_in_gb field
        :type backup_in_gb: object (optional)

        :param discount_rate: 折扣率，如 100 表示无折扣。
        :type discount_rate: int (optional)
        """
        super().__init__()
        self.price = price
        self.catalog_price = catalog_price
        self.traffic_in_gb = traffic_in_gb
        self.discount = discount
        self.real_catalog_price = real_catalog_price
        self.backup_in_gb = backup_in_gb
        self.discount_rate = discount_rate

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
        if self.price is not None:
            result['price'] = self.price
        if self.catalog_price is not None:
            result['catalogPrice'] = self.catalog_price
        if self.traffic_in_gb is not None:
            result['trafficInGB'] = self.traffic_in_gb
        if self.discount is not None:
            result['discount'] = self.discount
        if self.real_catalog_price is not None:
            result['realCatalogPrice'] = self.real_catalog_price
        if self.backup_in_gb is not None:
            result['backupInGB'] = self.backup_in_gb
        if self.discount_rate is not None:
            result['discountRate'] = self.discount_rate
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObtainThePriceDifferenceOfPrepaidTransformerResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('catalogPrice') is not None:
            self.catalog_price = m.get('catalogPrice')
        if m.get('trafficInGB') is not None:
            self.traffic_in_gb = m.get('trafficInGB')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('realCatalogPrice') is not None:
            self.real_catalog_price = m.get('realCatalogPrice')
        if m.get('backupInGB') is not None:
            self.backup_in_gb = m.get('backupInGB')
        if m.get('discountRate') is not None:
            self.discount_rate = m.get('discountRate')
        return self
