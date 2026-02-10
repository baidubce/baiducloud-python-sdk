
from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.reservation import Reservation


class Billing(AbstractModel):
    """
    Billing
    """
    def __init__(self, payment_timing=None, billing_method=None, reservation=None):
        super().__init__()
        self.payment_timing = payment_timing
        self.billing_method = billing_method
        self.reservation = reservation

    def to_dict(self):
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
        m = m or dict()
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('reservation') is not None:
            self.reservation = Reservation().from_dict(m.get('reservation'))
        return self
