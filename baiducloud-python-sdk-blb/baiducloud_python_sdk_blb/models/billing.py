"""
Billing information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.reservation import Reservation


class Billing(AbstractModel):
    """
    Billing
    """

    def __init__(self, payment_timing=None, billing_method=None, reservation=None):
        """
        Initialize Billing instance.

        :param payment_timing: 付款时间，预支付（Prepaid）和后支付（Postpaid）
        :type payment_timing: str (optional)

        :param billing_method: 计费方式，预付费的时候不要传，后付费的时候传，按固定规格计费（BySpec）和按使用量计费（ByCapacityUnit）
        :type billing_method: str (optional)

        :param reservation: reservation attribute
        :type reservation: Reservation (optional)
        """
        super().__init__()
        self.payment_timing = payment_timing
        self.billing_method = billing_method
        self.reservation = reservation

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.reservation is not None:
            result['reservation'] = self.reservation.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Billing

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('reservation') is not None:
            self.reservation = Reservation().from_dict(m.get('reservation'))
        return self
