"""
Request entity for GetPriceBySpecResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.spec_id_prices import SpecIdPrices


class GetPriceBySpecResponse(BceResponse):
    """
    GetPriceBySpecResponse
    """

    def __init__(self, price=None):
        """
        Initialize GetPriceBySpecResponse response.

        :param price: 实例套餐规格对应价格信息
        :type price: List[SpecIdPrices] (optional)
        """
        super().__init__()
        self.price = price

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
            result['price'] = [i.to_dict() for i in self.price]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPriceBySpecResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('price') is not None:
            self.price = [SpecIdPrices().from_dict(i) for i in m.get('price')]
        return self
