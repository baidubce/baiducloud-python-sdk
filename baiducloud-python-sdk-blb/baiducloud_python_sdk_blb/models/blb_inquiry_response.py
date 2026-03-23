"""
Request entity for BlbInquiryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_blb.models.price import Price


class BlbInquiryResponse(BceResponse):
    """
    BlbInquiryResponse
    """

    def __init__(self, prices=None):
        """
        Initialize BlbInquiryResponse response.

        :param prices: 返回的价格信息
        :type prices: List[Price] (optional)
        """
        super().__init__()
        self.prices = prices

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
            result['metadata'] = self.metadata
        if self.prices is not None:
            result['prices'] = [i.to_dict() for i in self.prices]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BlbInquiryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('prices') is not None:
            self.prices = [Price().from_dict(i) for i in m.get('prices')]
        return self
