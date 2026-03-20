"""
Request entity for EipInquiryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class EipInquiryResponse(BceResponse):
    """
    EipInquiryResponse
    """

    def __init__(self, prices=None):
        """
        Initialize EipInquiryResponse response.

        :param prices: 价格明细（包含purchasePrice（预付费价格）、configPrice（配置价格）、netrafficPrice（流量价格））
        :type prices: Dict[str, str] (optional)
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
            result['prices'] = self.prices
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipInquiryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('prices') is not None:
            self.prices = m.get('prices')
        return self
