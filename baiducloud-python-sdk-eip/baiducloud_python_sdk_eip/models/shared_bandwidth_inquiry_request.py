"""
Request entity for SharedBandwidthInquiryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing


class SharedBandwidthInquiryRequest(AbstractModel):
    """
    Request entity for SharedBandwidthInquiryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, bandwidth_in_mbps, ip_num, billing, count=None):
        """
        Initialize SharedBandwidthInquiryRequest request entity.

        :param bandwidth_in_mbps: 公网带宽，单位为Mbps。限制为为1~200之间的整数。
        :type bandwidth_in_mbps: int (required)

        :param count: 共享带宽的数量，默认为1。
        :type count: int (optional)

        :param ip_num: 共享带宽中的IP数量。
        :type ip_num: int (required)

        :param billing: billing parameter
        :type billing: Billing (required)
        """
        super().__init__()
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.count = count
        self.ip_num = ip_num
        self.billing = billing

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
        if self.ip_num is not None:
            result['ipNum'] = self.ip_num
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SharedBandwidthInquiryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('ipNum') is not None:
            self.ip_num = m.get('ipNum')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
