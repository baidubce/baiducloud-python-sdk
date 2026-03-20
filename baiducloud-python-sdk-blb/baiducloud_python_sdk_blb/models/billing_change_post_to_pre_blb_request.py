"""
Request entity for BillingChangePostToPreBlbRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BillingChangePostToPreBlbRequest(AbstractModel):
    """
    Request entity for BillingChangePostToPreBlbRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, reservation_length, client_token=None, billing_method=None, performance_level=None):
        """
        Initialize BillingChangePostToPreBlbRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing_method: 计费类型。当前只支持默认值\"BySpec\"。
        :type billing_method: str (optional)

        :param performance_level:
            性能规格。不填表示不进行配置变更。取值如下：\"small1\"标准型1，\"small2\"标准型2，\"medium1\"增强型1，\"medium2\"增强型2，\"large1\"超大型1，
            \"large2\"超大型2，\"large3\"超大型3。注意：预付费不支持\"unlimited\"不限速
        :type performance_level: str (optional)

        :param reservation_length: 购买月份时长，[1,2,3,4,5,6,7,8,9,12,24,36]
        :type reservation_length: int (required)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.billing_method = billing_method
        self.performance_level = performance_level
        self.reservation_length = reservation_length

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
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BillingChangePostToPreBlbRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        return self
