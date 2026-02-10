from baiducloud_python_sdk_core.abstract_model import AbstractModel

class SharedDataPackageInquiryRequest(AbstractModel):
    
    def __init__(self, reservation_length, capacity, client_token=None, deduct_policy=None, package_type=None):
        super().__init__()
        self.client_token = client_token
        self.reservation_length = reservation_length
        self.capacity = capacity
        self.deduct_policy = deduct_policy
        self.package_type = package_type

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.deduct_policy is not None:
            result['deductPolicy'] = self.deduct_policy
        if self.package_type is not None:
            result['packageType'] = self.package_type
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('deductPolicy') is not None:
            self.deduct_policy = m.get('deductPolicy')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        return self