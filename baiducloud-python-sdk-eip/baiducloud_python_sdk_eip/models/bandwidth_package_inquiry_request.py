"""
Request entity for BandwidthPackageInquiryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BandwidthPackageInquiryRequest(AbstractModel):
    """
    Request entity for BandwidthPackageInquiryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, bandwidth_in_mbps, count=None, type=None):
        """
        Initialize BandwidthPackageInquiryRequest request entity.

        :param bandwidth_in_mbps: 公网带宽，单位为Mbps。对于使用带宽计费的EIP，限制为为1~200之间的整数（代表带宽上限）。
        :type bandwidth_in_mbps: int (required)

        :param count: EIP数量，默认为1。
        :type count: int (optional)

        :param type: 带宽包的类型，包括BandwidthPackage（带宽包）和AccelerationPackage（跨境加速包），其中跨境加速包仅支持中国香港区域，默认为BandwidthPackage
        :type type: str (optional)
        """
        super().__init__()
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.count = count
        self.type = type

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.count is not None:
            result['count'] = self.count
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BandwidthPackageInquiryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
