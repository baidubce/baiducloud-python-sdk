
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RecycleEipModel(AbstractModel):
    """
    RecycleEipModel
    """
    def __init__(self, name=None, eip=None, eip_id=None, status=None, route_type=None, bandwidth_in_mbps=None, payment_timing=None, billing_method=None, recycle_time=None, scheduled_delete_time=None):
        super().__init__()
        self.name = name
        self.eip = eip
        self.eip_id = eip_id
        self.status = status
        self.route_type = route_type
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.payment_timing = payment_timing
        self.billing_method = billing_method
        self.recycle_time = recycle_time
        self.scheduled_delete_time = scheduled_delete_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.eip is not None:
            result['eip'] = self.eip
        if self.eip_id is not None:
            result['eipId'] = self.eip_id
        if self.status is not None:
            result['status'] = self.status
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.recycle_time is not None:
            result['recycleTime'] = self.recycle_time
        if self.scheduled_delete_time is not None:
            result['scheduledDeleteTime'] = self.scheduled_delete_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('eipId') is not None:
            self.eip_id = m.get('eipId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('recycleTime') is not None:
            self.recycle_time = m.get('recycleTime')
        if m.get('scheduledDeleteTime') is not None:
            self.scheduled_delete_time = m.get('scheduledDeleteTime')
        return self
