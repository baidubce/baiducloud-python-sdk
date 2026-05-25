"""
Request entity for BlbInquiryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.billing import Billing


class BlbInquiryRequest(AbstractModel):
    """
    Request entity for BlbInquiryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_type=None, performance_level=None, count=None, billing=None):
        """
        Initialize BlbInquiryRequest request entity.

        :param blb_type: blb类型，不传默认是普通型blb。
            取值可以为\"normal\"代表普通型，\"application\"代表应用型，\"ipv6\"代表普通型IPv6，\"ipv6Application\"代表应用型IPv6
        :type blb_type: str (optional)

        :param performance_level:
            性能规格参数，不传默认为共享型。取值如下：\"small1\"标准型1，\"small2\"标准型2，\"medium1\"增强型1，\"medium2\"增强型1，\"large1\"超大型1，
            \"large2\"超大型2，\"large3\"超大型3
        :type performance_level: str (optional)

        :param count: 购买数量，不传默认是1
        :type count: int (optional)

        :param billing: billing parameter
        :type billing: Billing (optional)
        """
        super().__init__()
        self.blb_type = blb_type
        self.performance_level = performance_level
        self.count = count
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
        if self.blb_type is not None:
            result['blbType'] = self.blb_type
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        if self.count is not None:
            result['count'] = self.count
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
        :rtype: BlbInquiryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbType') is not None:
            self.blb_type = m.get('blbType')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
