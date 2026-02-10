from baiducloud_python_sdk_core.abstract_model import AbstractModel

class CreateTbspRequest(AbstractModel):
    
    def __init__(self, name, line_type, ip_capacity, reservation_length, reservation_time_unit, client_token=None, auto_renew_time=None, auto_renew_time_unit=None):
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.line_type = line_type
        self.ip_capacity = ip_capacity
        self.reservation_length = reservation_length
        self.reservation_time_unit = reservation_time_unit
        self.auto_renew_time = auto_renew_time
        self.auto_renew_time_unit = auto_renew_time_unit

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.line_type is not None:
            result['lineType'] = self.line_type
        if self.ip_capacity is not None:
            result['ipCapacity'] = self.ip_capacity
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        if self.reservation_time_unit is not None:
            result['reservationTimeUnit'] = self.reservation_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('lineType') is not None:
            self.line_type = m.get('lineType')
        if m.get('ipCapacity') is not None:
            self.ip_capacity = m.get('ipCapacity')
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        if m.get('reservationTimeUnit') is not None:
            self.reservation_time_unit = m.get('reservationTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        return self