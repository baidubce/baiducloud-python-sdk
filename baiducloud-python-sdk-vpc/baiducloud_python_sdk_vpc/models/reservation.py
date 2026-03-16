
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Reservation(AbstractModel):
    """
    Reservation
    """
    def __init__(self, reservation_length=None, reservation_time_unit=None):
        super().__init__()
        self.reservation_length = reservation_length
        self.reservation_time_unit = reservation_time_unit

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        if self.reservation_time_unit is not None:
            result['reservationTimeUnit'] = self.reservation_time_unit
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        if m.get('reservationTimeUnit') is not None:
            self.reservation_time_unit = m.get('reservationTimeUnit')
        return self
