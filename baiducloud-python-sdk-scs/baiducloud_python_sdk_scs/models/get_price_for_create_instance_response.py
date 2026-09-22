"""
Request entity for GetPriceForCreateInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetPriceForCreateInstanceResponse(BceResponse):
    """
    GetPriceForCreateInstanceResponse
    """

    def __init__(self, price=None, catalog_price=None):
        """
        Initialize GetPriceForCreateInstanceResponse response.

        :param price: price field
        :type price: float (optional)

        :param catalog_price: 目录价。单位同price一致。
        :type catalog_price: float (optional)
        """
        super().__init__()
        self.price = price
        self.catalog_price = catalog_price

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
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPriceForCreateInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('catalogPrice') is not None:
            self.catalog_price = m.get('catalogPrice')
        return self
