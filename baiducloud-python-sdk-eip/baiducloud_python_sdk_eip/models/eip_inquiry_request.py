"""
Request entity for EipInquiryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing


class EipInquiryRequest(AbstractModel):
    """
    Request entity for EipInquiryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, bandwidth_in_mbps, billing, count=None, purchase_type=None):
        """
        Initialize EipInquiryRequest request entity.

        :param bandwidth_in_mbps:
            公网带宽，单位为Mbps。对于使用带宽计费的EIP，限制为为1~200之间的整数（代表带宽上限）；对于按使用流量计费的EIP，限制为1~1000之间的整数（代表允许的带宽流量峰值）。
        :type bandwidth_in_mbps: int (required)

        :param count: EIP数量，默认为1.
        :type count: int (optional)

        :param purchase_type: EIP购买线路选择，可选择BGP、Static、ChinaTelcom、ChinaUnicom、ChinaMobile，默认BGP
        :type purchase_type: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)
        """
        super().__init__()
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.count = count
        self.purchase_type = purchase_type
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
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
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
        :rtype: EipInquiryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
