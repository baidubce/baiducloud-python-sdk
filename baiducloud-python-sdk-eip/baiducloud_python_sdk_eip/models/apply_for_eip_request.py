from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing
from baiducloud_python_sdk_eip.models.tag_model import TagModel

class ApplyForEipRequest(AbstractModel):
    
    def __init__(self, client_token, bandwidth_in_mbps, billing, ip_version=None, route_type=None, name=None, tags=None, resource_group_id=None, auto_renew_time_unit=None, auto_renew_time=None, delete_protect=None):
        super().__init__()
        self.client_token = client_token
        self.ip_version = ip_version
        self.route_type = route_type
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.billing = billing
        self.name = name
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time
        self.delete_protect = delete_protect

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self