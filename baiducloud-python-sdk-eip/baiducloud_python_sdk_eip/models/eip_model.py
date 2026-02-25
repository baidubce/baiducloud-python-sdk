
from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.tag_model import TagModel


class EipModel(AbstractModel):
    """
    EipModel
    """
    def __init__(self, name=None, eip=None, eip_id=None, status=None, eip_instance_type=None, instance_type=None, instance_id=None, share_group_id=None, default_domestic_bandwidth=None, bandwidth_in_mbps=None, bw_short_id=None, bw_bandwidth_in_mbps=None, domestic_bw_short_id=None, domestic_bw_bandwidth_in_mbps=None, payment_timing=None, billing_method=None, create_time=None, expire_time=None, region=None, route_type=None, tags=None, delete_protect=None, native_group=None, original_bandwidth=None, origin_product_type=None, origin_sub_product_type=None):
        super().__init__()
        self.name = name
        self.eip = eip
        self.eip_id = eip_id
        self.status = status
        self.eip_instance_type = eip_instance_type
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.share_group_id = share_group_id
        self.default_domestic_bandwidth = default_domestic_bandwidth
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.bw_short_id = bw_short_id
        self.bw_bandwidth_in_mbps = bw_bandwidth_in_mbps
        self.domestic_bw_short_id = domestic_bw_short_id
        self.domestic_bw_bandwidth_in_mbps = domestic_bw_bandwidth_in_mbps
        self.payment_timing = payment_timing
        self.billing_method = billing_method
        self.create_time = create_time
        self.expire_time = expire_time
        self.region = region
        self.route_type = route_type
        self.tags = tags
        self.delete_protect = delete_protect
        self.native_group = native_group
        self.original_bandwidth = original_bandwidth
        self.origin_product_type = origin_product_type
        self.origin_sub_product_type = origin_sub_product_type

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
        if self.eip_instance_type is not None:
            result['eipInstanceType'] = self.eip_instance_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.share_group_id is not None:
            result['shareGroupId'] = self.share_group_id
        if self.default_domestic_bandwidth is not None:
            result['defaultDomesticBandwidth'] = self.default_domestic_bandwidth
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.bw_short_id is not None:
            result['bwShortId'] = self.bw_short_id
        if self.bw_bandwidth_in_mbps is not None:
            result['bwBandwidthInMbps'] = self.bw_bandwidth_in_mbps
        if self.domestic_bw_short_id is not None:
            result['domesticBwShortId'] = self.domestic_bw_short_id
        if self.domestic_bw_bandwidth_in_mbps is not None:
            result['domesticBwBandwidthInMbps'] = self.domestic_bw_bandwidth_in_mbps
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.region is not None:
            result['region'] = self.region
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        if self.native_group is not None:
            result['nativeGroup'] = self.native_group
        if self.original_bandwidth is not None:
            result['originalBandwidth'] = self.original_bandwidth
        if self.origin_product_type is not None:
            result['originProductType'] = self.origin_product_type
        if self.origin_sub_product_type is not None:
            result['originSubProductType'] = self.origin_sub_product_type
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
        if m.get('eipInstanceType') is not None:
            self.eip_instance_type = m.get('eipInstanceType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('shareGroupId') is not None:
            self.share_group_id = m.get('shareGroupId')
        if m.get('defaultDomesticBandwidth') is not None:
            self.default_domestic_bandwidth = m.get('defaultDomesticBandwidth')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('bwShortId') is not None:
            self.bw_short_id = m.get('bwShortId')
        if m.get('bwBandwidthInMbps') is not None:
            self.bw_bandwidth_in_mbps = m.get('bwBandwidthInMbps')
        if m.get('domesticBwShortId') is not None:
            self.domestic_bw_short_id = m.get('domesticBwShortId')
        if m.get('domesticBwBandwidthInMbps') is not None:
            self.domestic_bw_bandwidth_in_mbps = m.get('domesticBwBandwidthInMbps')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        if m.get('nativeGroup') is not None:
            self.native_group = m.get('nativeGroup')
        if m.get('originalBandwidth') is not None:
            self.original_bandwidth = m.get('originalBandwidth')
        if m.get('originProductType') is not None:
            self.origin_product_type = m.get('originProductType')
        if m.get('originSubProductType') is not None:
            self.origin_sub_product_type = m.get('originSubProductType')
        return self
