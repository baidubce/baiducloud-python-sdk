"""
Request entity for DescribePriceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.price_info import PriceInfo


class DescribePriceResponse(BceResponse):
    """
    DescribePriceResponse
    """

    def __init__(self, price_infos=None):
        """
        Initialize DescribePriceResponse response.

        :param price_infos: 价格信息，见附录 PriceInfo
        :type price_infos: List[PriceInfo] (optional)
        """
        super().__init__()
        self.price_infos = price_infos

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
        if self.price_infos is not None:
            result['priceInfos'] = [i.to_dict() for i in self.price_infos]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribePriceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('priceInfos') is not None:
            self.price_infos = [PriceInfo().from_dict(i) for i in m.get('priceInfos')]
        return self
